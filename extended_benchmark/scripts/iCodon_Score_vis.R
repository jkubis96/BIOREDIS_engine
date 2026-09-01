library(iCodon)
library(readxl)

table <- read_xlsx('../data/random_CDS_jbst_extended_full.xlsx')

score_base <- iCodon::predict_stability('human')


table$native_iCodon <- NA
table$jbst_iCodon <- NA
table$vectorbuilder_iCodon <- NA
table$codontransformer_iCodon <- NA
table$genscript_iCodon <- NA




for (s in 1:nrow(table)) {
  table$native_iCodon[s] <- score_base(table$seq[s])
  table$jbst_iCodon[s] <- score_base(table$jbst_sequence[s])
  table$vectorbuilder_iCodon[s] <- score_base(table$vectorbuilder_sequence[s])
  table$codontransformer_iCodon[s] <- score_base(table$codontransformer_sequence[s])
  table$genscript_iCodon[s] <- score_base(table$genscript_sequence[s])
  


}




library(writexl)
write_xlsx(table, path = "../data/random_CDS_jbst_extended_iScore.xlsx")


new_table <- data.frame(
  gene_id = table$id,
  gene_name = table$gene_name,
  sequence = table$seq,
  category = table$type,
  GC = table$gc,
  MFE = table$mfe,
  iCodonScore = table$native_iCodon,
  CodonFrequence = table$frequence

)

new_table$source <- 'Native'


for (i in c('CodonTransformer', 'GenScript', 'VectorBuilder', 'BIOREDIS-engine')) {
  
  if (i == 'BIOREDIS-engine') {
    
    tmp <- data.frame(
      gene_id = table$id,
      gene_name = table$gene_name,
      sequence = table$seq,
      category = table$type,
      GC = table[[paste0(tolower('jbst'),'_gc')]],
      MFE = table[[paste0(tolower('jbst'),'_mfe')]],
      iCodonScore = table[[paste0(tolower('jbst'),'_iCodon')]],
      CodonFrequence = table[[paste0(tolower('jbst'),'_frequence')]]
      
    )
    
    tmp$source <- 'BIOREDIS-engine'
    new_table <- rbind(new_table, tmp)
    next
    
  }
    tmp <- data.frame(
    gene_id = table$id,
    gene_name = table$gene_name,
    sequence = table$seq,
    category = table$type,
    GC = table[[paste0(tolower(i),'_gc')]],
    MFE = table[[paste0(tolower(i),'_mfe')]],
    iCodonScore = table[[paste0(tolower(i),'_iCodon')]],
    CodonFrequence = table[[paste0(tolower(i),'_frequence')]]
    
  )
  
  tmp$source <- i
  new_table <- rbind(new_table, tmp)
  }


write_xlsx(new_table, path = "../data/random_CDS_jbst_extended_iScore_long_stats.xlsx")


library(ggplot2)
library(dplyr)
library(tidyr)
library(patchwork)


df_long <- new_table %>%
  pivot_longer(cols = c(GC, MFE, iCodonScore, CodonFrequence), 
               names_to = "Metric", 
               values_to = "Value") %>%
  mutate(source = factor(source, levels = c(
    "Native", 
    "CodonTransformer", 
    "GenScript", 
    "VectorBuilder", 
    "BIOREDIS-engine"
  )))

line_data <- data.frame(
  Metric = "GC",
  yintercept = 60
)

g <- ggplot(df_long, aes(x = category, y = Value, fill = source)) +
  stat_summary(fun = mean, geom = "bar", position = position_dodge(width = 0.75), 
               width = 0.7, alpha = 0.7, color = "grey40", linewidth = 0.3) +
  
  stat_summary(
    data = df_long,
    fun.data = mean_se, 
    geom = "errorbar",
    position = position_dodge(width = 0.75),
    width = 0.25,
    linewidth = 0.4,
    color = "grey30"
  )+
  geom_hline(data = line_data, aes(yintercept = yintercept), 
             color = "red", linetype = "42", linewidth = 0.4) +
  facet_wrap(~ Metric, scales = "free_y") +
  theme_bw(base_size = 12) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    x = NULL, 
    y = "Value", 
    fill = ""
  ) +
  theme(
    axis.text.x = element_text(angle = 25, hjust = 1, face = "bold"),
    legend.position = "bottom",
    strip.background = element_rect(fill = "grey95", color = "grey80"),
    strip.text = element_text(face = "bold", size = 11),
    panel.grid.minor = element_blank()
  )

dev.off()
svg(filename = "../fig/codon_optimization.svg", width = 8, height = 6)

g

dev.off()

source("https://raw.githubusercontent.com/jkubis96/JStatML-R/main/scripts/statML-R.R")


for (s in unique(new_table$category)) {
  
  tmp <- new_table[new_table$category %in% s,]
  
  result <- multi_groups_analysis(value_column = 'GC', 
                                  grouping_column = 'source', 
                                  data = tmp, 
                                  bar_queue = c("Native", 
                                                "CodonTransformer", 
                                                "GenScript", 
                                                "VectorBuilder", 
                                                "BIOREDIS-engine"), 
                                  x_label = 'Group', 
                                  x_angle = 30, 
                                  y_label = 'Value', 
                                  size = 1, 
                                  parametric = TRUE, 
                                  include_ns = FALSE, 
                                  bars = 'sem', 
                                  bars_size = 1,
                                  bar_size = 0.5,
                                  stat_plot_ratio = 0.45,
                                  stat_hight = 0.6,
                                  adjustment.method = 'none', 
                                  y_break = NA, 
                                  brew_colors = 'Dark2'
                                  
  )
  
  
  svg(filename = paste0("../fig/codon_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),"_GC.svg"), width = 6.3, height = 4)
  
  
  g <- result@box_plot + geom_hline(yintercept = 60, color = "red", linetype = "dashed", linewidth = 0.6)
  print(g)
  
  
  dev.off()
  

  


  result <- multi_groups_analysis(value_column = 'MFE', 
                                  grouping_column = 'source', 
                                  data = tmp, 
                                  bar_queue = c("Native", 
                                                "CodonTransformer", 
                                                "GenScript", 
                                                "VectorBuilder", 
                                                "BIOREDIS-engine"), 
                                  x_label = 'Group', 
                                  x_angle = 30, 
                                  y_label = 'Value', 
                                  size = 1, 
                                  parametric = TRUE, 
                                  include_ns = FALSE, 
                                  bars = 'sem', 
                                  bars_size = 1,
                                  bar_size = 0.5,
                                  stat_plot_ratio = 0.45,
                                  stat_hight = 0,
                                  adjustment.method = 'none', 
                                  y_break = NA, 
                                  brew_colors = 'Dark2'
                                  
  )
  
  
  svg(filename = paste0("../fig/codon_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),"_MFE.svg"), width = 6.3, height = 4)
  
  print(result@box_plot)
  
  
  dev.off()
  
  
  result <- multi_groups_analysis(value_column = 'iCodonScore', 
                                  grouping_column = 'source', 
                                  data = tmp, 
                                  bar_queue = c("Native", 
                                                "CodonTransformer", 
                                                "GenScript", 
                                                "VectorBuilder", 
                                                "BIOREDIS-engine"), 
                                  x_label = 'Group', 
                                  x_angle = 30, 
                                  y_label = 'Value', 
                                  size = 1, 
                                  parametric = TRUE, 
                                  include_ns = FALSE, 
                                  bars = 'sem', 
                                  bars_size = 1,
                                  bar_size = 0.5,
                                  stat_plot_ratio = 0.45,
                                  stat_hight = 0.6,
                                  adjustment.method = 'none', 
                                  y_break = NA, 
                                  brew_colors = 'Dark2'
                                  
  )
  
  
  svg(filename = paste0("../fig/codon_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),"_iCodonScore.svg"), width = 6.3, height = 4)
  
  print(result@box_plot)
  
  
  dev.off()
  
  
  
  result <- multi_groups_analysis(value_column = 'CodonFrequence', 
                                  grouping_column = 'source', 
                                  data = tmp, 
                                  bar_queue = c("Native", 
                                                "CodonTransformer", 
                                                "GenScript", 
                                                "VectorBuilder", 
                                                "BIOREDIS-engine"), 
                                  x_label = 'Group', 
                                  x_angle = 30, 
                                  y_label = 'Value', 
                                  size = 1, 
                                  parametric = TRUE, 
                                  include_ns = FALSE, 
                                  bars = 'sem', 
                                  bars_size = 1,
                                  bar_size = 0.5,
                                  stat_plot_ratio = 0.45,
                                  stat_hight = 0.6,
                                  adjustment.method = 'none', 
                                  y_break = NA, 
                                  brew_colors = 'Dark2'
                                  
  )
  
  
  svg(filename = paste0("../fig/codon_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),"_CodonFrequence.svg"), width = 6.3, height = 4)
  
  print(result@box_plot)
  
  
  dev.off()
  
  
  
  result <- multi_groups_analysis(value_column = 'CodonFrequence', 
                                  grouping_column = 'source', 
                                  data = tmp, 
                                  bar_queue = c("Native", 
                                                "CodonTransformer", 
                                                "GenScript", 
                                                "VectorBuilder", 
                                                "BIOREDIS-engine"), 
                                  x_label = 'Group', 
                                  x_angle = 30, 
                                  y_label = 'Value', 
                                  size = 1, 
                                  parametric = TRUE, 
                                  include_ns = FALSE, 
                                  bars = 'sem', 
                                  bars_size = 1,
                                  bar_size = 0.5,
                                  stat_plot_ratio = 0.45,
                                  stat_hight = 0.6,
                                  adjustment.method = 'none', 
                                  y_break = NA, 
                                  brew_colors = 'Dark2'
                                  
  )
  
  
  svg(filename = paste0("../fig/codon_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),"_CodonFrequence.svg"), width = 6.3, height = 4)
  
  print(result@box_plot)
  
  
  dev.off()
  
  
  
}

################################################################################



actg_table <- data.frame()

for (i in c('CodonTransformer', 'GenScript', 'VectorBuilder', 'BIOREDIS-engine')) {
  
  if (i == 'BIOREDIS-engine') {
    
    tmp  <- data.frame(
      `mean(A)` = mean(table[[paste0(tolower('jbst'),'_A_max[n]')]]),
      `mean(C)` = mean(table[[paste0(tolower('jbst'),'_C_max[n]')]]),
      `mean(T)` = mean(table[[paste0(tolower('jbst'),'_T_max[n]')]]),
      `mean(G)` = mean(table[[paste0(tolower('jbst'),'_G_max[n]')]])
      

      
    )
    
    tmp$source <- 'BIOREDIS-engine'
    actg_table <- rbind(actg_table, tmp)
    
    next
    
  }
  tmp  <- data.frame(
    `mean(A)` = mean(table[[paste0(tolower(i),'_A_max[n]')]]),
    `mean(C)` = mean(table[[paste0(tolower(i),'_C_max[n]')]]),
    `mean(T)` = mean(table[[paste0(tolower(i),'_T_max[n]')]]),
    `mean(G)` = mean(table[[paste0(tolower(i),'_G_max[n]')]])
    
    
  )
    
  
  tmp$source <- i
  actg_table <- rbind(actg_table, tmp)
}

write_xlsx(actg_table, path = "../data/random_CDS_jbst_extended_actg_table.xlsx")



library(pheatmap)
library(RColorBrewer)

heatmap_matrix <- as.matrix(actg_table[, 1:4])
rownames(heatmap_matrix) <- actg_table$source

my_bordeaux_palette <- colorRampPalette(c("#FFF5F0", "#FB6A4A", "#A50F15", "#67000D"))(50)

p <- pheatmap(
  heatmap_matrix, 
  cluster_rows = TRUE,      
  cluster_cols = TRUE,      
  display_numbers = TRUE,   
  number_color = "black",   
  color = my_bordeaux_palette, 
  angle_col = 45,
)

dev.off()
svg(filename = "../fig/homopolimers_Clustermap.svg", width = 8, height = 6)

p

dev.off()

###########################################################################




#################################################################################


library(dplyr)
library(readxl)

check <- read_xlsx('../sources/check_list_mrna.xlsx')

count_matches <- function(pattern, sequences) {
  sum(sapply(sequences, function(x) {
    m <- gregexpr(pattern, x, fixed = TRUE)[[1]]
    if (m[1] == -1) 0 else length(m)
  }))
}


check_df <- data.frame(
  motif = check$Sequence,
  category = check$Category,
  Native = sapply(check$Sequence, count_matches, sequences = table$seq),
  JBioSeqTool = sapply(check$Sequence, count_matches, sequences = table$jbst_sequence),
  VectorBuilder = sapply(check$Sequence, count_matches, sequences = table$vectorbuilder_sequence),
  CodonTransformer = sapply(check$Sequence, count_matches, sequences = table$codontransformer_sequence),
  GenScript = sapply(check$Sequence, count_matches, sequences = table$genscript_sequence) # poprawiłem literówkę z dwukrotnego codontransformer
)

check_summary_df <- check_df %>%
  group_by(category) %>%
  summarise(
    Native = sum(Native),
    `BIOREDIS-engine` = sum(JBioSeqTool),
    VectorBuilder = sum(VectorBuilder),
    CodonTransformer = sum(CodonTransformer),
    GenScript = sum(GenScript),
    .groups = 'drop'
  )


write_xlsx(check_df, path = "../data/motifs_sequences.xlsx")
write_xlsx(check_summary_df, path = "../data/motifs.xlsx")

print(check_summary_df)


library(pheatmap)
library(RColorBrewer)

heatmap_matrix <- as.matrix(check_summary_df[, -1])
rownames(heatmap_matrix) <- check_summary_df$category

my_bordeaux_palette <- colorRampPalette(c("#FFF5F0", "#FB6A4A", "#A50F15", "#67000D"))(50)

p <- pheatmap(
  heatmap_matrix, 
  cluster_rows = TRUE,      
  cluster_cols = TRUE,      
  display_numbers = TRUE,   
  number_format = "%.0f",   
  number_color = "black",   
  color = my_bordeaux_palette, 
  angle_col = 45,
)

dev.off()
svg(filename = "../fig/mRNA_Motifs_Clustermap.svg", width = 8, height = 6)

p

dev.off()

###########################################################################



###########################################################################

# od tutaj!!


library(ggplot2)
library(dplyr)
library(tidyr)
library(patchwork)
library(readxl)

table_rnai <- read_xlsx('../data/random_CDS_jbst_RNAi_top1_with_jbst_with_statistics.xlsx')





df_long <- table_rnai %>%
  pivot_longer(cols = c(GC, score, 
                        `DSIR_corrected-score`,
                        iSCORE,
                        complemenatry_pct, 
                        repeated_motif_pct), 
               names_to = "Metric", 
               values_to = "Value") 





colnames(table_rnai)[colnames(table_rnai) %in% 'DSIR_corrected-score'] <- 'DSIR-corrected-score'
colnames(table_rnai)[colnames(table_rnai) %in% 'score'] <- 'BIOREDIS-score'
colnames(table_rnai)[colnames(table_rnai) %in% 'repeated_motif_pct'] <- 'Homopolimer-motifs'
colnames(table_rnai)[colnames(table_rnai) %in% 'complemenatry_pct'] <- 'Complementary-motifs'


metric_order <- c("DSIR-corrected-score", "iSCORE", "BIOREDIS-score", "GC", 
                  "Homopolimer-motifs", "Complementary-motifs")

df_long <- table_rnai %>%
  pivot_longer(
    cols = c(GC, `BIOREDIS-score`, `DSIR-corrected-score`, iSCORE, `Complementary-motifs`, `Homopolimer-motifs`),
    names_to = "Metric",
    values_to = "Value"
  ) %>%
  mutate(Metric = factor(Metric, levels = metric_order))



df_long$source2 <- gsub('-.*$', '', df_long$source)
df_long$nuc <- gsub('^.*-', '', df_long$source)


df_long$source2 <- gsub('_.*$', '', df_long$source2)
df_long$nuc <- gsub('^.*_', '', df_long$nuc) 

df_long$source2 = gsub('JBST', 'BIOREDIS-engine', df_long$source2)


df_long$nuc <- paste0(df_long$nuc, " nuc")

df_long <- df_long %>%
  mutate(source2 = factor(
    source2,
    levels = c(
      "OligoShell", 
      "InvivoGene", 
      "GenScript", 
      "VectorBuilder", 
      "BIOREDIS-engine"
    )
  ))

line_data <- data.frame(
  Metric = factor(c("GC", "GC"), levels = metric_order),
  yintercept = c(35, 60)
)

g <- ggplot(df_long, aes(x = nuc, y = Value, fill = source2)) +
  stat_summary(
    data = subset(df_long, Metric != "GC"),
    fun = mean, 
    geom = "bar", 
    position = position_dodge(width = 0.75), 
    width = 0.7, 
    alpha = 0.7, 
    color = "grey40", 
    linewidth = 0.3
  ) +
  stat_summary(
    data = subset(df_long, Metric != "GC"),
    fun.data = mean_se, 
    geom = "errorbar",
    position = position_dodge(width = 0.75),
    width = 0.25,
    linewidth = 0.4,
    color = "grey30"
  ) +
  geom_boxplot(
    data = subset(df_long, Metric == "GC"),
    position = position_dodge(width = 0.75), 
    width = 0.6, 
    alpha = 0.7, 
    color = "grey40", 
    linewidth = 0.4,
    outlier.size = 1.2,
    outlier.alpha = 0.6
  ) +
  geom_hline(
    data = line_data, 
    aes(yintercept = yintercept), 
    color = "red", 
    linetype = "dashed", 
    linewidth = 0.5
  ) +
  facet_wrap(~ Metric, scales = "free_y") +
  scale_y_continuous(expand = expansion(mult = c(0.05, 0.1))) +
  theme_bw(base_size = 12) +
  scale_fill_brewer(palette = "Set2") +
  labs(
    x = NULL, 
    y = "Value", 
    fill = ""
  ) +
  theme(
    axis.text.x = element_text(angle = 25, hjust = 1, face = "bold"),
    legend.position = "bottom",
    strip.background = element_rect(fill = "grey95", color = "grey80"),
    strip.text = element_text(face = "bold", size = 11),
    panel.grid.minor = element_blank()
  )

print(g)

dev.off()
svg(filename = "../fig/rnai_score.svg", width = 8, height = 6)

g

dev.off()




table_rnai <- read_xlsx('../data/random_CDS_jbst_RNAi_top1_with_jbst_with_statistics.xlsx')




colnames(table_rnai)[colnames(table_rnai) %in% 'DSIR_corrected-score'] <- 'DSIR_corrected_score'
colnames(table_rnai)[colnames(table_rnai) %in% 'score'] <- 'BIOREDIS_score'
colnames(table_rnai)[colnames(table_rnai) %in% 'repeated_motif_pct'] <- 'Homopolimer_motifs'
colnames(table_rnai)[colnames(table_rnai) %in% 'complemenatry_pct'] <- 'Complementary_motifs'


metric_order <- c("DSIR_corrected_score", "iSCORE", "BIOREDIS_score", "GC", 
                  "Homopolimer_motifs", "Complementary_motifs")

source("https://raw.githubusercontent.com/jkubis96/JStatML-R/main/scripts/statML-R.R")




table_rnai$source <- gsub('JBST_', 'BIOREDIS_engine-', table_rnai$source )

for (s in unique(metric_order)) {

  if (s == 'iSCORE') {
    
    result <- multi_groups_analysis(value_column = s, 
                                    grouping_column = 'source', 
                                    data = table_rnai[grepl('19', table_rnai$source),], 
                                    bar_queue = c("GenScript-19",
                                                  "InvivoGene-19",
                                                  "OligoShell-19",
                                                  "BIOREDIS_engine-19"
                                    ), 
                                    x_label = 'Group', 
                                    x_angle = 30, 
                                    y_label = 'Value', 
                                    size = 1, 
                                    parametric = TRUE, 
                                    include_ns = FALSE, 
                                    bars = 'sem', 
                                    bars_size = 1,
                                    bar_size = 0.5,
                                    stat_plot_ratio = 0.45,
                                    stat_hight = 0.6,
                                    adjustment.method = 'none', 
                                    y_break = NA, 
                                    brew_colors = 'Dark2'
                                    
    )
    
  } else {
    
    result <- multi_groups_analysis(value_column = s, 
                                    grouping_column = 'source', 
                                    data = table_rnai, 
                                    bar_queue = c("GenScript-19",
                                                  "VectorBuilder-21",
                                                  "InvivoGene-19",
                                                  "InvivoGene-21",
                                                  "OligoShell-19",
                                                  "OligoShell-21",
                                                  "BIOREDIS_engine-19",
                                                  "BIOREDIS_engine-21"
                                    ), 
                                    x_label = 'Group', 
                                    x_angle = 30, 
                                    y_label = 'Value', 
                                    size = 1, 
                                    parametric = TRUE, 
                                    include_ns = FALSE, 
                                    bars = 'sem', 
                                    bars_size = 1,
                                    bar_size = 0.5,
                                    stat_plot_ratio = 0.45,
                                    stat_hight = 0.6,
                                    adjustment.method = 'none', 
                                    y_break = NA, 
                                    brew_colors = 'Dark2'
                                    
    )
    
    
  }
  
  
  
  svg(filename = paste0("../fig/rnai_supplement/",sub('\\s*\\|\\s*', '_', gsub(' ', '_', s)),".svg"), width = 6.3, height = 4)
  
  if (s == 'GC') {
    
    g <- result@box_plot + 
      geom_hline(yintercept = 60, color = "red", linetype = "dashed", linewidth = 0.6) + 
      geom_hline(yintercept = 35, color = "blue", linetype = "dashed", linewidth = 0.6)
    print(g)
  } else {
    
    print(result@box_plot) 
      
  }
  
 
  
  dev.off()
  
  
  
  
  
  
}

