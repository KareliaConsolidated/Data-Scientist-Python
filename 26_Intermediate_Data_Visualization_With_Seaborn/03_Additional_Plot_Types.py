############### Exercise ###############
# stripplot() and swarmplot()
# Many datasets have categorical data and Seaborn supports several useful plot types for this data. In this example, we will continue to look at the 2010 School Improvement data and segment the data by the types of school improvement models used.

# As a refresher, here is the KDE distribution of the Award Amounts:

# Image Ref 01

# While this plot is useful, there is a lot more we can learn by looking at the individual Award_Amounts and how they are distributed among the 4 categories.
############### Instructions ###############
# Create a stripplot of the Award_Amount with the Model Selected on the y axis with jitter enabled.

# Create the stripplot
sns.stripplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         jitter=True)

plt.show()

############### Instructions ###############
# Create a swarmplot() of the same data, but also include the hue by Region.
# Create and display a swarmplot with hue set to the Region
sns.swarmplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         hue='Region')

plt.show()

############### Exercise ###############
# boxplots, violinplots and lvplots
# Seaborn's categorical plots also support several abstract representations of data. The API for each of these is the same so it is very convenient to try each plot and see if the data lends itself to one over the other.

# In this exercise, we will use the color palette options presented in Chapter 2 to show how colors can easily be included in the plots.

############### Instructions ###############
# Create and display a boxplot of the data with Award_Amount on the x axis and Model Selected on the y axis.
# Create a boxplot
sns.boxplot(data=df,
         x='Award_Amount',
         y='Model Selected')

plt.show()
plt.clf()

############### Instructions ###############
# Create and display a similar violinplot of the data, but use the husl palette for colors.
# Create a violinplot with the husl palette
sns.violinplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='husl')

plt.show()
plt.clf()

############### Instructions ###############
# Create a lvplot with the Paired palette and the Region column as the hue
sns.lvplot(data=df,
         x='Award_Amount',
         y='Model Selected',
         palette='Paired',
         hue='Region')

plt.show()
plt.clf()

############### Exercise ###############
# barplots, pointplots and countplots
# The final group of categorical plots are barplots, pointplots and countplot which create statistical summaries of the data. The plots follow a similar API as the other plots and allow further customization for the specific problem at hand.

############### Instructions ###############
# Create a countplot with the df dataframe and Model Selected on the y axis and the color varying by Region.
# Show a countplot with the number of models used with each region a different color
sns.countplot(data=df,
         y="Model Selected",
         hue="Region")

plt.show()
plt.clf()
############### Instructions ###############
# Create a pointplot with the df dataframe and Model Selected on the x-axis and Award_Amount on the y-axis.
# Use a capsize in the pointplot in order to show the confidence interval.
# Create a pointplot and include the capsize in order to show bars on the confidence interval
sns.pointplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         capsize=.1)

plt.show()
plt.clf()
############### Instructions ###############
# Create a barplot with the same data on the x and y axis and change the color of each bar based on the Region column.

# Create a barplot with each Region shown as a different color
sns.barplot(data=df,
         y='Award_Amount',
         x='Model Selected',
         hue='Region')

plt.show()
plt.clf()

############### Exercise ###############
# Regression and residual plots
# Linear regression is a useful tool for understanding the relationship between numerical variables. Seaborn has simple but powerful tools for examining these relationships.

# For these exercises, we will look at some details from the US Department of Education on 4 year college tuition information and see if there are any interesting insights into which variables might help predict tuition costs.

# For these exercises, all data is loaded in the df variable.

############### Instructions ###############
# Plot a regression plot comparing Tuition and average SAT scores(SAT_AVG_ALL).
# Make sure the values are shown as green triangles.
# Display a regression plot for Tuition
sns.regplot(data=df,
         y='Tuition',
         x="SAT_AVG_ALL",
         marker='^',
         color='g')

plt.show()
plt.clf()

############### Instructions ###############
# Use a residual plot to determine if the relationship looks linear.
# Display the residual plot
sns.residplot(data=df,
          y='Tuition',
          x="SAT_AVG_ALL",
          color='g')

plt.show()
plt.clf()

############### Exercise ###############
# Regression plot parameters
# Seaborn's regression plot supports several parameters that can be used to configure the plots and drive more insight into the data.

# For the next exercise, we can look at the relationship between tuition and the percent of students that receive Pell grants. A Pell grant is based on student financial need and subsidized by the US Government. In this data set, each University has some percentage of students that receive these grants. Since this data is continuous, using x_bins can be useful to break the percentages into categories in order to summarize and understand the data.

############### Instructions ###############
# Plot a regression plot of Tuition and PCTPELL.
# Plot a regression plot of Tuition and the Percentage of Pell Grants
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL")

plt.show()

############### Instructions ###############
# Create another plot that estimates the tuition by PCTPELL
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5)

plt.show()
plt.clf()
plt.clf()

############### Instructions ###############
# The final plot should include a line using a 2nd order polynomial
sns.regplot(data=df,
            y='Tuition',
            x="PCTPELL",
            x_bins=5,
            order=2)

plt.show()
plt.clf()

############### Exercise ###############
# Binning data
# When the data on the x axis is a continuous value, it can be useful to break it into different bins in order to get a better visualization of the changes in the data.

# For this exercise, we will look at the relationship between tuition and the Undergraduate population abbreviated as UG in this data. We will start by looking at a scatter plot of the data and examining the impact of different bin sizes on the visualization.

############### Instructions ###############
# Create a regplot of Tuition and UG and set the fit_reg parameter to False to disable the regression line.

# Create a scatter plot by disabling the regression line
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            fit_reg=False)

plt.show()
plt.clf()

############### Instructions ###############
# Create another plot with the UG data divided into 5 bins.
# Create a scatter plot and bin the data into 5 bins
sns.regplot(data=df,
            y='Tuition',
            x="UG",
            x_bins=5)

plt.show()
plt.clf()

############### Instructions ###############

# Create a regplot() with the data divided into 8 bins.

# Create a regplot and bin the data into 8 bins
sns.regplot(data=df,
         y='Tuition',
         x="UG",
         x_bins=8)

plt.show()
plt.clf()

############### Exercise ###############
# Creating heatmaps
# A heatmap is a common matrix plot that can be used to graphically summarize the relationship between two variables. For this exercise, we will start by looking at guests of the Daily Show from 1999 - 2015 and see how the occupations of the guests have changed over time.

# The data includes the date of each guest appearance as well as their occupation. For the first exercise, we need to get the data into the right format for Seaborn's heatmap function to correctly plot the data. All of the data has already been read into the df variable.

############### Instructions ###############
# Use pandas' crosstab() function to build a table of visits by Group and Year.
# Print the pd_crosstab DataFrame.
# Plot the data using Seaborn's heatmap().

# Create a crosstab table of the data
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])
print(pd_crosstab)

# Plot a heatmap of the table
sns.heatmap(pd_crosstab)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

plt.show()

############### Exercise ###############
# Customizing heatmaps
# Seaborn supports several types of additional customizations to improve the output of a heatmap. For this exercise, we will continue to use the Daily Show data that is stored in the df variable but we will customize the output.

############### Instructions ###############
# Create a crosstab table of Group and YEAR
# Create a heatmap of the data using the BuGn palette
# Disable the cbar and increase the linewidth to 0.3

# Create the crosstab DataFrame
pd_crosstab = pd.crosstab(df["Group"], df["YEAR"])

# Plot a heatmap of the table with no color bar and using the BuGn palette
sns.heatmap(pd_crosstab, cbar=False, cmap="BuGn", linewidths=0.3)

# Rotate tick marks for visibility
plt.yticks(rotation=0)
plt.xticks(rotation=90)

#Show the plot
plt.show()
plt.clf()