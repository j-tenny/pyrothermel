import pyrothermel

# Initialize model framework
fuel_models = pyrothermel.FuelModels()
mortality_species_table = pyrothermel.SpeciesMasterTable()
behave = pyrothermel.BehaveRun(fuel_models, mortality_species_table)

# Set input values
fuel_model_number = 20
custom_fuel_model = True

# Custom fuel model parameters
code = "Custom"
name = "CustomFuelModel"
fuel_bed_depth = 0.5
length_units = pyrothermel.LengthUnits.Meters
moisture_of_extinction_dead = 0.3
moisture_units = pyrothermel.FractionUnits.Fraction
heat_of_combustion_dead = 8000
heat_of_combustion_live = 8000
heat_of_combustion_units = pyrothermel.HeatOfCombustionUnits.BtusPerPound
fuel_load_one_hour = 0.08
fuel_load_ten_hour = 0.08
fuel_load_hundred_hour = 0.08
fuel_load_live_herbaceous = 0.08
fuel_load_live_woody = 0.08
loading_units = pyrothermel.LoadingUnits.KilogramsPerSquareMeter
savr_one_hour = 2000
savr_live_herbaceous = 2000
savr_live_woody = 1600
savr_units = pyrothermel.SurfaceAreaToVolumeUnits.SquareInchesOverCubicInches
is_dynamic = False

if custom_fuel_model:
    fuel_models.setCustomFuelModel(
        fuel_model_number, code, name, fuel_bed_depth, length_units, moisture_of_extinction_dead,
        moisture_units, heat_of_combustion_dead, heat_of_combustion_live, heat_of_combustion_units,
        fuel_load_one_hour, fuel_load_ten_hour, fuel_load_hundred_hour, fuel_load_live_herbaceous,
        fuel_load_live_woody, loading_units, savr_one_hour, savr_live_herbaceous, savr_live_woody,
        savr_units, is_dynamic
    )

# Update inputs in model objects
moisture_one_hour = 0.05
moisture_ten_hour = 0.07
moisture_hundred_hour = 0.09
moisture_live_herbaceous = 0.6
moisture_live_woody = 0.90
wind_speed = 20
wind_speed_units = pyrothermel.SpeedUnits.MilesPerHour
wind_height_input_mode = pyrothermel.WindHeightInputMode.DirectMidflame
wind_direction = 42

slope = 30
aspect = 291
canopy_cover = 0.50  # 50%
canopy_cover_units = pyrothermel.FractionUnits.Fraction
canopy_height = 6
canopy_height_units = pyrothermel.LengthUnits.Meters
crown_ratio = 0.50

wind_and_spread_orientation_mode = pyrothermel.WindAndSpreadOrientationMode.RelativeToNorth

behave.surface.updateSurfaceInputs(
    fuel_model_number, moisture_one_hour, moisture_ten_hour, moisture_hundred_hour,
    moisture_live_herbaceous, moisture_live_woody, moisture_units, wind_speed, wind_speed_units,
    wind_height_input_mode, wind_direction, wind_and_spread_orientation_mode, slope,
    pyrothermel.SlopeUnits.Degrees, aspect, canopy_cover, canopy_cover_units, canopy_height,
    canopy_height_units, crown_ratio, pyrothermel.FractionUnits.Fraction
)

behave.surface.setIsUsingChaparral(False)

# Run model with given inputs
behave.surface.doSurfaceRunInDirectionOfMaxSpread()

# Get results
spread_rate = behave.surface.getSpreadRate(pyrothermel.SpeedUnits.KilometersPerHour)
print(f"Rate of spread: {spread_rate} km/hr")
flame_length = behave.surface.getFlameLength(pyrothermel.LengthUnits.Meters)
print(f"Flame length: {flame_length} meters")
direction_of_max_spread = behave.surface.getDirectionOfMaxSpread()
print(f"Direction of maximum spread is {direction_of_max_spread} degrees")

# Run scorch model
fireline_intensity = behave.surface.getFirelineIntensity(pyrothermel.FirelineIntensityUnits.BtusPerFootPerSecond)
midflame_windspeed = behave.surface.getMidflameWindspeed(pyrothermel.SpeedUnits.MilesPerHour)
air_temperature = 80.0
scorch_length_units = pyrothermel.LengthUnits.Meters
observed_scorch_height = behave.mortality.calculateScorchHeight(
    fireline_intensity, pyrothermel.FirelineIntensityUnits.BtusPerFootPerSecond,
    midflame_windspeed, pyrothermel.SpeedUnits.MilesPerHour,
    air_temperature, pyrothermel.TemperatureUnits.Fahrenheit,
    scorch_length_units
)
print(f"Scorch height is {observed_scorch_height} meters")

# Run crown model
moisture_foliar = 1
canopy_base_height = 2.952756
canopy_bulk_density = 0.1
canopy_bulk_density_units = pyrothermel.DensityUnits.KilogramsPerCubicMeter

behave.crown.setWindAdjustmentFactorCalculationMethod(pyrothermel.WindAdjustmentFactorCalculationMethod.UserInput)
behave.crown.setUserProvidedWindAdjustmentFactor(0.4)
behave.crown.updateCrownInputs(
    fuel_model_number, moisture_one_hour, moisture_ten_hour, moisture_hundred_hour,
    moisture_live_herbaceous, moisture_live_woody, moisture_foliar, moisture_units, wind_speed,
    wind_speed_units, wind_height_input_mode, wind_direction, wind_and_spread_orientation_mode, slope,
    pyrothermel.SlopeUnits.Degrees, aspect, canopy_cover, canopy_cover_units, canopy_height,
    canopy_base_height, canopy_height_units, crown_ratio, pyrothermel.FractionUnits.Fraction,
    canopy_bulk_density, canopy_bulk_density_units
)

behave.crown.doCrownRunScottAndReinhardt()
crown_fire_spread_rate = behave.crown.getFinalSpreadRate(pyrothermel.SpeedUnits.KilometersPerHour)
print(f"Crown fire spread rate is {crown_fire_spread_rate} km/hr")
crown_fire_intensity = behave.crown.getFinalFirelineIntensity(pyrothermel.FirelineIntensityUnits.KilowattsPerMeter)
print(f"Crown fire intensity is {crown_fire_intensity}")
crown_fire_flame_length = behave.crown.getCrownFlameLength(pyrothermel.LengthUnits.Meters)
print(f"Crown fire flame length is {crown_fire_flame_length}")
transition_ratio = behave.crown.getTransitionRatio()
print(f"Transition ratio is {transition_ratio}")
active_ratio = behave.crown.getActiveRatio()
print(f"Active ratio is {active_ratio}")
fire_type = behave.crown.getFireType()
print(f"Fire type is {fire_type}")