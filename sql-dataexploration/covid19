
Select *
From PortfolioProject..CovidDeaths
Where continent is not null
order by 3,4



-- Select data to begin with

Select Location,
       date,
       total_cases,
       new_cases,
       total_deaths,
       population
From PortfolioProject..CovidDeaths
Where continent is not null
order by 1,2



-- Total cases vs Total deaths
-- An indicator to know how likely somebody is going to die if they contact Covid

Select Location,
       date,
       total_cases,
       total_deaths,
       (CAST(total_deaths AS float)/CAST(total_cases AS float))*100 AS "%Death"
From PortfolioProject..CovidDeaths
Where continent is not null
order by 1,2



-- Total cases vs Population
-- Shows what percentage of population infected with Covid

Select Location,
       date,
       population,
       total_cases,
       (total_cases/population)*100 as "%Infected"
From PortfolioProject..CovidDeaths
Where location like '%India%' and continent is not null
order by 1,2



-- Countries with Highest Infection Rate compared to Population

Select Location,
       population,
       MAX(cast(total_cases as int)) as HighestCount,
       MAX(total_cases/population)*100 as "%Infected"
From PortfolioProject..CovidDeaths
Where continent is not null
Group by Location, population
Order by [%Infected] DESC



-- Countries with Highest Death Count per Population

Select Location,
       MAX(cast(total_deaths as int)) as TotalDeathToll
From PortfolioProject..CovidDeaths
Where continent is not null
Group by Location
Order by TotalDeathToll DESC



-- BREAKING THINGS DOWN BY CONTINENT
-- Contintents with the highest death count per population

Select location,
       MAX(cast(total_deaths as int)) as TotalDeathToll
From PortfolioProject..CovidDeaths
Where continent is null
Group by location
Order by TotalDeathToll DESC



-- Global Stats

Select date,
       SUM(new_cases) as TotalCases,
       SUM(new_deaths) as TotalDeaths,
       CASE When SUM(new_cases) > 0 
            Then SUM(new_deaths) / SUM(new_cases) * 100 
            Else 0 end as "%Death"
From PortfolioProject..CovidDeaths
Where continent is not null
Group by date
Order by 1,2



-- Total Cases and Total Deaths

Select SUM(new_cases) as TotalCases,
       SUM(new_deaths) as TotalDeaths,
       CASE When SUM(new_cases) > 0 
            Then SUM(new_deaths) / SUM(new_cases) * 100 
            Else 0 end as "%Death"
From PortfolioProject..CovidDeaths
Where continent is not null
Order by 1,2



-- Population vs Total Vaccinations
-- Shows Percentage of Population that has recieved at least one dose of Vaccine

Select ded.continent,
       ded.location,
       ded.date,
       ded.population,
       vax.new_vaccinations,
       SUM(CONVERT(bigint, vax.new_vaccinations)) OVER (Partition by ded.location Order by ded.location, ded.date) as VaxxCounts
From PortfolioProject..CovidDeaths ded
Join PortfolioProject..CovidVaxx vax
     On ded.location = vax.location
     and ded.date = vax.date
Where ded.continent is not null
Order by 2,3



-- Using CTE to perform Calculation on Partition By in previous query

With PopvsVax (Continent, Location, Date, Population, new_vaccinations, VaxxCounts)
as
(
Select ded.continent,
       ded.location,
       ded.date,
       ded.population,
       vax.new_vaccinations,
       SUM(CONVERT(bigint, vax.new_vaccinations)) OVER (Partition by ded.location Order by ded.location, ded.date) as VaxxCounts
From PortfolioProject..CovidDeaths ded
Join PortfolioProject..CovidVaxx vax
     On ded.location = vax.location
     and ded.date = vax.date
Where ded.continent is not null
)
Select *, (VaxxCounts/Population)*100 as "%Vaxxed"
From PopvsVax



-- Using Temp Table to perform Calculation on Partition By in previous query

DROP Table if exists #PercentPopulationGotVaccinated
Create Table #PercentPopulationGotVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
VaxxCounts numeric
)


Insert into #PercentPopulationGotVaccinated
Select ded.continent,
       ded.location,
       ded.date,
       ded.population,
       vax.new_vaccinations,
       SUM(CONVERT(bigint, vax.new_vaccinations)) OVER (Partition by ded.location Order by ded.location, ded.date) as VaxxCounts
From PortfolioProject..CovidDeaths ded
Join PortfolioProject..CovidVaxx vax
     On ded.location = vax.location
     and ded.date = vax.date


Select *, (VaxxCounts/Population)*100 as "%Vaxxed"
From #PercentPopulationGotVaccinated



-- Creating View to store data for later visualizations

USE PortfolioProject
GO
Create View PercentPopulationGotVaccinated as 
Select ded.continent,
       ded.location,
       ded.date,
       ded.population,
       vax.new_vaccinations,
       SUM(CONVERT(bigint, vax.new_vaccinations)) OVER (Partition by ded.location Order by ded.location, ded.date) as VaxxCounts
From PortfolioProject..CovidDeaths ded
Join PortfolioProject..CovidVaxx vax
     On ded.location = vax.location
     and ded.date = vax.date
Where ded.continent is not null


Select *
From PercentPopulationGotVaccinated
