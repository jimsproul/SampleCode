-- List Sales Person by Order of Their Contribution
--
-- SQL Server Version: SQL Server 2019
--			 Data Use: Microsoft's [AdventureWorks2019]
--
-- This demonstration query (c) Jim Sproul 2024
--
-- First create a common table expression (CTE) to calculate
--    each peron's YTD sales
--
WITH [TotalSales] AS
	(SELECT p.BusinessEntityID
		    ,p.[FirstName]
			,p.[LastName]
			,SUM(sp.[SalesYTD]) OVER(PARTITION BY p.[FirstName], p.[LastName]) AS [Total YTD Sales]
		FROM [AdventureWorks2019].[Sales].[SalesPerson] sp
		JOIN [AdventureWorks2019].[Person].[Person] p ON p.[BusinessEntityID] = sp.[BusinessEntityID])
--
-- Now use the results of the CTE to determine the each
--    person's YTD total sales with the sales leader's total
--
select ts.[FirstName] as [First Name]
		,ts.[LastName] as [Last Name]
		,FORMAT(ROUND(ts.[Total YTD Sales],2),'C','en-us') AS [Total YTD Sales]
		,FORMAT(ROUND(MAX(ts.[Total YTD Sales]) OVER(),2),'C','en-us') AS [Sales  Leader(s) YTD Sales]
		,(ts.[Total YTD Sales]/MAX(ts.[Total YTD Sales]) OVER())*100 AS [% of Sales  Leader(s)]
		, ROW_NUMBER() OVER( ORDER BY ts.[Total YTD Sales] DESC)  AS [Sales Leader(s) Rank]
	FROM [TotalSales] ts 
ORDER BY 2,1 DESC

