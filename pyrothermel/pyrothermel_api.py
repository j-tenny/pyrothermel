from example import transition_ratio
from pyrothermel import behave_core, units, modes
from typing import Union

_FM_INDEX = 255

class PyrothermelRun:
    def __init__(self, fuel_model, moisture_scenario, wind_speed, units_preset='metric', wind_input_mode='direct_midflame', wind_direction=0, slope=0., aspect=0, air_temperature=None, canopy_base_height = None, canopy_bulk_density = None, canopy_cover=None, canopy_height=None, canopy_ratio=None):
        # Instantiate objects required by behave_core
        self._fuel_models = behave_core.FuelModels()
        self._mortality_species_table = behave_core.SpeciesMasterTable()

        # Instantiate objects where default value is None
        self.canopy_base_height = None
        self.canopy_bulk_density = None
        self.canopy_cover = None
        self.canopy_height = None
        self.canopy_ratio = None
        self.units = _get_units_preset(units_preset)
        if air_temperature is None:
            if self.units.temperature_units == units.TemperatureUnits.Celsius:
                air_temperature = 30.
            elif self.units.temperature_units == units.TemperatureUnits.Fahrenheit:
                air_temperature = 85.
            elif self.units.temperature_units == units.TemperatureUnits.Kelvin:
                air_temperature = 302.

        # Set values using user-provided and/or default values
        self.update_inputs(fuel_model=fuel_model, moisture_scenario=moisture_scenario, wind_speed=wind_speed, units_preset=units_preset, wind_input_mode=wind_input_mode, wind_direction=wind_direction, slope=slope, aspect=aspect, air_temperature=air_temperature,canopy_base_height=canopy_base_height,canopy_bulk_density=canopy_bulk_density, canopy_cover=canopy_cover, canopy_height=canopy_height, canopy_ratio=canopy_ratio)

    def update_inputs(self,fuel_model=None, moisture_scenario=None, wind_speed=None, units_preset=None, wind_input_mode=None, wind_direction=None, slope=None, aspect=None, air_temperature=None, canopy_base_height=None, canopy_bulk_density=None, canopy_cover=None, canopy_height=None, canopy_ratio=None):

        if units_preset is not None:
            self.units = _get_units_preset(units_preset)
        if moisture_scenario is not None:
            self.moisture_scenario = moisture_scenario
        if wind_speed is not None:
            self.wind_speed = wind_speed
        if wind_input_mode is not None:
            self.wind_input_mode = wind_input_mode
        if wind_direction is not None:
            self.wind_direction = wind_direction
        if slope is not None:
            self.slope = slope
        if aspect is not None:
            self.aspect = aspect
        if air_temperature is not None:
            self.air_temperature = air_temperature
        if canopy_bulk_density is not None:
            self.canopy_bulk_density = canopy_bulk_density
        if canopy_base_height is not None:
            self.canopy_base_height = canopy_base_height
        if canopy_cover is not None:
            self.canopy_cover = canopy_cover
        if canopy_height is not None:
            self.canopy_height = canopy_height
        if canopy_ratio is not None:
            self.canopy_ratio = canopy_ratio


        self.wind_input_mode, canopy_cover, canopy_height, canopy_ratio = self._validate_wind_input_mode(self.wind_input_mode,
                                                                                                    self.canopy_cover,
                                                                                                    self.canopy_height,
                                                                                                    self.canopy_ratio)


        self._update_fuel_model(fuel_model)

        self._run = behave_core.BehaveRun(self._fuel_models, self._mortality_species_table)

        self._run.surface.updateSurfaceInputs(_FM_INDEX,
                                              self.moisture_scenario.moisture_one_hour,
                                              self.moisture_scenario.moisture_ten_hour,
                                              self.moisture_scenario.moisture_hundred_hour,
                                              self.moisture_scenario.moisture_live_herbaceous,
                                              self.moisture_scenario.moisture_live_woody,
                                              self.moisture_scenario.units,
                                              self.wind_speed,
                                              self.units.windspeed_units,
                                              self.wind_input_mode,
                                              self.wind_direction,
                                              modes.WindAndSpreadOrientationMode.RelativeToNorth,
                                              self.slope,
                                              self.units.slope_units,
                                              self.aspect,
                                              canopy_cover,
                                              self.units.fraction_units,
                                              canopy_height,
                                              self.units.length_units,
                                              canopy_ratio,
                                              self.units.fraction_units)


    def _update_fuel_model(self,fuel_model=None):
        if fuel_model is not None:
            self.fuel_model = fuel_model
        self._fuel_models.setCustomFuelModel(_FM_INDEX,
                                             self.fuel_model.code,
                                             self.fuel_model.name,
                                             self.fuel_model.fuel_bed_depth,
                                             self.fuel_model.units.length_units,
                                             self.fuel_model.moisture_of_extinction_dead,
                                             self.fuel_model.units.fraction_units,
                                             self.fuel_model.heat_of_combustion_dead,
                                             self.fuel_model.heat_of_combustion_live,
                                             self.fuel_model.units.heat_of_combustion_units,
                                             self.fuel_model.fuel_load_one_hour,
                                             self.fuel_model.fuel_load_ten_hour,
                                             self.fuel_model.fuel_load_hundred_hour,
                                             self.fuel_model.fuel_load_live_herbaceous,
                                             self.fuel_model.fuel_load_live_woody,
                                             self.fuel_model.units.loading_units,
                                             self.fuel_model.savr_one_hour,
                                             self.fuel_model.savr_live_herbaceous,
                                             self.fuel_model.savr_live_woody,
                                             self.fuel_model.units.savr_units,
                                             self.fuel_model.is_dynamic)

    def _validate_wind_input_mode(self,wind_input_mode,canopy_cover,canopy_height,canopy_ratio):
        wind_input_mode = _validate_wind_input_mode(wind_input_mode, canopy_cover, canopy_height, canopy_ratio)

        if self.canopy_cover is None:
            canopy_cover = 0
        else:
            canopy_cover = self.canopy_cover

        if self.canopy_height is None:
            canopy_height = 0
        else:
            canopy_height = self.canopy_height

        if self.canopy_ratio is None:
            canopy_ratio = 0
        else:
            canopy_ratio = self.canopy_ratio

        return [wind_input_mode,canopy_cover,canopy_height,canopy_ratio]

    def run_surface_fire_in_direction_of_max_spread(self):
        self.update_inputs()
        self._run.surface.doSurfaceRunInDirectionOfMaxSpread()
        self.spread_rate = self._run.surface.getSpreadRate(self.units.spread_rate_units)
        self.flame_length = self._run.surface.getFlameLength(self.units.length_units)
        self.fireline_intensity = self._run.surface.getFirelineIntensity(self.units.fireline_intensity_units)
        self.midflame_windspeed = self._run.surface.getMidflameWindspeed(self.units.windspeed_units)
        self.direction_of_max_spread = self._run.surface.getDirectionOfMaxSpread()
        self.scorch_height = self._run.mortality.calculateScorchHeight(self.fireline_intensity, self.units.fireline_intensity_units,
                                                                      self.midflame_windspeed, self.units.windspeed_units, self.air_temperature,
                                                                      self.units.temperature_units, self.units.length_units)
        results = {'spread_rate': self.spread_rate,'flame_length':self.flame_length,
                   'fireline_intensity':self.fireline_intensity,'scorch_height':self.scorch_height}
        return results

    def run_surface_fire_in_direction_of_interest(self, direction):
        self.update_inputs()
        self._run.surface.doSurfaceRunInDirectionOfInterest(direction,modes.WindAndSpreadOrientationMode.RelativeToNorth)
        self.spread_rate = self._run.surface.getSpreadRate(self.units.spread_rate_units)
        self.flame_length = self._run.surface.getFlameLength(self.units.length_units)
        self.fireline_intensity = self._run.surface.getFirelineIntensity(self.units.fireline_intensity_units)
        self.midflame_windspeed = self._run.surface.getMidflameWindspeed(self.units.windspeed_units)
        self.direction_of_max_spread = self._run.surface.getDirectionOfMaxSpread()
        self.scorch_height = self._run.mortality.calculateScorchHeight(self.fireline_intensity, self.units.fireline_intensity_units,
                                                                      self.midflame_windspeed, self.units.windspeed_units, self.air_temperature,
                                                                      self.units.temperature_units, self.units.length_units)
        results = {'spread_rate': self.spread_rate,'flame_length':self.flame_length,
                   'fireline_intensity':self.fireline_intensity,'scorch_height':self.scorch_height}
        return results

    def run_crown_fire_scott_and_reinhardt(self):
        if self.canopy_base_height is None or self.canopy_bulk_density is None:
            raise ValueError('canopy_base_height and canopy_bulk_density must be provided')

        wind_input_mode, canopy_cover, canopy_height, canopy_ratio = self._validate_wind_input_mode(self.wind_input_mode, self.canopy_cover, self.canopy_height, self.canopy_ratio)

        self._run.crown.updateCrownInputs(_FM_INDEX, self.moisture_scenario.moisture_one_hour,
                                           self.moisture_scenario.moisture_ten_hour,
                                           self.moisture_scenario.moisture_hundred_hour,
                                           self.moisture_scenario.moisture_live_herbaceous,
                                           self.moisture_scenario.moisture_live_woody,
                                           self.moisture_scenario.foliar_moisture, self.moisture_scenario.units,
                                           self.wind_speed, self.units.windspeed_units,
                                           self.wind_input_mode, self.wind_direction, modes.WindAndSpreadOrientationMode.RelativeToNorth,
                                           self.slope, self.units.slope_units, self.aspect, canopy_cover,
                                           self.units.fraction_units, canopy_height, self.canopy_base_height,
                                           self.units.length_units, canopy_ratio, self.units.fraction_units,
                                           self.canopy_bulk_density, self.units.density_units
                                        )
        self._run.crown.doCrownRunScottAndReinhardt()

        self.spread_rate = self._run.crown.getFinalSpreadRate(self.units.spread_rate_units)
        self.fireline_intensity = self._run.crown.getFinalFirelineIntensity(self.units.fireline_intensity_units)
        self.flame_length = self._run.crown.getFinalFlameLength(self.units.length_units)
        self.transition_ratio = self._run.crown.getTransitionRatio()
        self.active_ratio = self._run.crown.getActiveRatio()
        self.fire_type = self._run.crown.getFireType()

        results = {'spread_rate': self.spread_rate,'flame_length':self.flame_length,
                   'fireline_intensity':self.fireline_intensity, 'scorch_height':self.scorch_height,
                   'transition_ratio':self.transition_ratio, 'active_ratio':self.active_ratio,'fire_type':self.fire_type}
        return results

    def run_crown_fire_rothermel(self):
        if self.canopy_base_height is None or self.canopy_bulk_density is None:
            raise ValueError('canopy_base_height and canopy_bulk_density must be provided')

        wind_input_mode, canopy_cover, canopy_height, canopy_ratio = self._validate_wind_input_mode(
            self.wind_input_mode, self.canopy_cover, self.canopy_height, self.canopy_ratio)

        self._run.crown.updateCrownInputs(_FM_INDEX, self.moisture_scenario.moisture_one_hour,
                                          self.moisture_scenario.moisture_ten_hour,
                                          self.moisture_scenario.moisture_hundred_hour,
                                          self.moisture_scenario.moisture_live_herbaceous,
                                          self.moisture_scenario.moisture_live_woody,
                                          self.moisture_scenario.foliar_moisture, self.moisture_scenario.units,
                                          self.wind_speed, self.units.windspeed_units,
                                          self.wind_input_mode, self.wind_direction,
                                          modes.WindAndSpreadOrientationMode.RelativeToNorth,
                                          self.slope, self.units.slope_units, self.aspect, canopy_cover,
                                          self.units.fraction_units, canopy_height, self.canopy_base_height,
                                          self.units.length_units, canopy_ratio, self.units.fraction_units,
                                          self.canopy_bulk_density, self.units.density_units
                                          )
        self._run.crown.doCrownRunScottAndReinhardt()

        self.spread_rate = self._run.crown.getFinalSpreadRate(self.units.spread_rate_units)
        self.fireline_intensity = self._run.crown.getFinalFirelineIntensity(self.units.fireline_intensity_units)
        self.flame_length = self._run.crown.getCrownFinalFlameLength(self.units.length_units)
        self.transition_ratio = self._run.crown.getTransitionRatio()
        self.active_ratio = self._run.crown.getActiveRatio()
        self.fire_type = self._run.crown.getFireType()

        results = {'spread_rate': self.spread_rate, 'flame_length': self.flame_length,
                   'fireline_intensity': self.fireline_intensity, 'scorch_height': self.scorch_height,
                   'transition_ratio': self.transition_ratio, 'active_ratio': self.active_ratio,
                   'fire_type': self.fire_type}
        return results

    def calculate_torching_index(self, max_wind_speed=99, step=1):
        for wind_speed in range(0, max_wind_speed, step):
            self.update_inputs(wind_speed=wind_speed)
            self.run_surface_fire_in_direction_of_max_spread()
            results = self.run_crown_fire_scott_and_reinhardt()
            if results['transition_ratio']>=1:
                return wind_speed
        return wind_speed

    def calculate_crowning_index(self, max_wind_speed=99, step=1):
        for wind_speed in range(0, max_wind_speed, step):
            self.update_inputs(wind_speed=wind_speed)
            self.run_surface_fire_in_direction_of_max_spread()
            results = self.run_crown_fire_scott_and_reinhardt()
            if results['active_ratio']>=1:
                return wind_speed
        return wind_speed

class UnitsPreset:
    def __init__(self, area_units, basal_area_units, length_units, loading_units, savr_units, pressure_units, spread_rate_units,
                 windspeed_units, fraction_units, slope_units, density_units, heat_of_combustion_units,
                 heat_sink_units, heat_per_unit_area_units, heat_source_and_reaction_intensity_units,
                 fireline_intensity_units, temperature_units, time_units):

        self.area_units = area_units
        self.basal_area_units = basal_area_units
        self.length_units = length_units
        self.loading_units = loading_units
        self.savr_units = savr_units
        self.pressure_units = pressure_units
        self.spread_rate_units = spread_rate_units
        self.windspeed_units = windspeed_units
        self.fraction_units = fraction_units
        self.slope_units = slope_units
        self.density_units = density_units
        self.heat_of_combustion_units = heat_of_combustion_units
        self.heat_sink_units = heat_sink_units
        self.heat_per_unit_area_units = heat_per_unit_area_units
        self.heat_source_and_reaction_intensity_units = heat_source_and_reaction_intensity_units
        self.fireline_intensity_units = fireline_intensity_units
        self.temperature_units = temperature_units
        self.time_units = time_units

    @classmethod
    def metric(cls):
        preset = cls(units.AreaUnits.SquareMeters, units.BasalAreaUnits.SquareMetersPerHectare, units.LengthUnits.Meters,
                     units.LoadingUnits.KilogramsPerSquareMeter, units.SurfaceAreaToVolumeUnits.SquareMetersOverCubicMeters,
                     units.PressureUnits.KiloPascal, units.SpeedUnits.KilometersPerHour, units.SpeedUnits.KilometersPerHour,
                     units.FractionUnits.Fraction, units.SlopeUnits.Degrees, units.DensityUnits.KilogramsPerCubicMeter,
                     units.HeatOfCombustionUnits.KilojoulesPerKilogram, units.HeatSinkUnits.KilojoulesPerCubicMeter,
                     units.HeatPerUnitAreaUnits.KilojoulesPerSquareMeter, units.HeatSourceAndReactionIntensityUnits.KilowattsPerSquareMeter,
                     units.FirelineIntensityUnits.KilowattsPerMeter, units.TemperatureUnits.Celsius, units.TimeUnits.Hours)
        return preset

    @classmethod
    def us_standard(cls):
        preset = cls(units.AreaUnits.Acres, units.BasalAreaUnits.SquareFeetPerAcre, units.LengthUnits.Feet,
                     units.LoadingUnits.TonsPerAcre, units.SurfaceAreaToVolumeUnits.SquareFeetOverCubicFeet,
                     units.PressureUnits.PoundPerSquareInch, units.SpeedUnits.ChainsPerHour, units.SpeedUnits.MilesPerHour,
                     units.FractionUnits.Fraction, units.SlopeUnits.Degrees, units.DensityUnits.PoundsPerCubicFoot,
                     units.HeatOfCombustionUnits.BtusPerPound, units.HeatSinkUnits.BtusPerCubicFoot,
                     units.HeatPerUnitAreaUnits.BtusPerSquareFoot, units.HeatSourceAndReactionIntensityUnits.BtusPerSquareFootPerSecond,
                     units.FirelineIntensityUnits.BtusPerFootPerSecond, units.TemperatureUnits.Fahrenheit, units.TimeUnits.Hours)
        return preset

def _get_units_preset(units_preset) -> 'UnitsPreset':
    if type(units_preset) is UnitsPreset:
       return units_preset
    elif units_preset == 'metric':
        return UnitsPreset.metric()
    elif units_preset == 'us_standard':
        return UnitsPreset.us_standard()
    else:
        raise ValueError("units_preset must be 'metric' or 'us_standard' or UnitsPreset object")

def _validate_wind_input_mode(wind_input_mode, canopy_cover, canopy_height, canopy_ratio):
    if type(wind_input_mode) is not modes.WindHeightInputMode:
        if wind_input_mode == 'direct_midflame':
            wind_input_mode = modes.WindHeightInputMode.DirectMidflame
        elif wind_input_mode == 'ten_meter':
            wind_input_mode = modes.WindHeightInputMode.TenMeter
        elif wind_input_mode == 'twenty_foot':
            wind_input_mode = modes.WindHeightInputMode.TwentyFoot
        else:
            raise ValueError("wind_input_mode must be 'direct_midflame', 'ten_meter', or 'twenty_foot'")

    if wind_input_mode != modes.WindHeightInputMode.DirectMidflame:
        if canopy_ratio is None or canopy_height is None or canopy_cover is None:
            raise ValueError(
                "Canopy ratio, canopy height, and canopy cover must be provided if wind_input_mode is not 'direct_midflame'")

    return wind_input_mode

class FuelModel:
    def __init__(self,
                 units_preset,
                fuel_model_number: int,
                code: str,
                name: str,
                fuel_bed_depth: float,
                moisture_of_extinction_dead: float,
                heat_of_combustion_dead: float,
                heat_of_combustion_live: float,
                fuel_load_one_hour: float,
                fuel_load_ten_hour: float,
                fuel_load_hundred_hour: float,
                fuel_load_live_herbaceous: float,
                fuel_load_live_woody: float,
                savr_one_hour: float,
                savr_live_herbaceous: float,
                savr_live_woody: float,
                is_dynamic: bool,
    ) -> None:
        """
        Sets the fuel model record with the provided parameters.

        Args:
            units_preset: can be 'metric', 'us_standard', or a UnitsPreset object
            fuel_model_number (int): The fuel model number.
            code (str): The code representing the fuel model.
            name (str): The name of the fuel model.
            fuel_bed_depth (float): Depth of the fuel bed.
            moisture_of_extinction_dead (float): Moisture of extinction for dead fuels.
            heat_of_combustion_dead (float): Heat of combustion for dead fuels.
            heat_of_combustion_live (float): Heat of combustion for live fuels.
            fuel_load_one_hour (float): Fuel load for one-hour interval.
            fuel_load_ten_hour (float): Fuel load for ten-hour interval.
            fuel_load_hundred_hour (float): Fuel load for hundred-hour interval.
            fuel_load_live_herbaceous (float): Live herbaceous fuel load.
            fuel_load_live_woody (float): Live woody fuel load.
            savr_one_hour (float): Surface area-to-volume ratio for one-hour fuels.
            savr_live_herbaceous (float): Surface area-to-volume ratio for live herbaceous fuels.
            savr_live_woody (float): Surface area-to-volume ratio for live woody fuels.
            is_dynamic (bool): Indicates if the model is dynamic.
        """
        self.units = _get_units_preset(units_preset)
        self.fuel_model_number = fuel_model_number
        self.code = code
        self.name = name
        self.fuel_bed_depth = fuel_bed_depth
        self.moisture_of_extinction_dead = moisture_of_extinction_dead
        self.heat_of_combustion_dead = heat_of_combustion_dead
        self.heat_of_combustion_live = heat_of_combustion_live
        self.fuel_load_one_hour = fuel_load_one_hour
        self.fuel_load_ten_hour = fuel_load_ten_hour
        self.fuel_load_hundred_hour = fuel_load_hundred_hour
        self.fuel_load_live_herbaceous = fuel_load_live_herbaceous
        self.fuel_load_live_woody = fuel_load_live_woody
        self.savr_one_hour = savr_one_hour
        self.savr_live_herbaceous = savr_live_herbaceous
        self.savr_live_woody = savr_live_woody
        self.is_dynamic = is_dynamic

    @classmethod
    def from_existing(cls,identifier,units_preset='metric')->'FuelModel':
        units_preset = _get_units_preset(units_preset)
        fuelModels = behave_core.FuelModels()
        if type(identifier) is not int:
            for i in range(220):
                code = fuelModels.getFuelCode(i)
                if (identifier == code):
                    identifier = i
                    break
            if i == 219:
                raise ValueError("Could not find model matching this identifier")

        mod = cls(units_preset, identifier,
                  fuelModels.getFuelCode(identifier),
                  fuelModels.getFuelName(identifier),
                  fuelModels.getFuelbedDepth(identifier,units_preset.length_units),
                  fuelModels.getMoistureOfExtinctionDead(identifier,units_preset.fraction_units),
                  fuelModels.getHeatOfCombustionDead(identifier,units_preset.heat_of_combustion_units),
                  fuelModels.getHeatOfCombustionLive(identifier,units_preset.heat_of_combustion_units),
                  fuelModels.getFuelLoadOneHour(identifier,units_preset.loading_units),
                  fuelModels.getFuelLoadTenHour(identifier,units_preset.loading_units),
                  fuelModels.getFuelLoadHundredHour(identifier,units_preset.loading_units),
                  fuelModels.getFuelLoadLiveHerbaceous(identifier,units_preset.loading_units),
                  fuelModels.getFuelLoadLiveWoody(identifier,units_preset.loading_units),
                  fuelModels.getSavrOneHour(identifier,units_preset.savr_units),
                  fuelModels.getSavrLiveHerbaceous(identifier,units_preset.savr_units),
                  fuelModels.getSavrLiveWoody(identifier,units_preset.savr_units),
                  fuelModels.getIsDynamic(identifier))

        return mod

class MoistureScenario:
    def __init__(self, moisture_one_hour:float, moisture_ten_hour:float, moisture_hundred_hour:float, moisture_live_herbaceous:float, moisture_live_woody:float, foliar_moisture = 1, fraction_units='fraction'):

        if type(fraction_units) != units.FractionUnits.FractionUnitsEnum:
            if fraction_units == 'fraction':
                fraction_units = units.FractionUnits.Fraction
            elif fraction_units == 'percent':
                fraction_units = units.FractionUnits.Percent
            else:
                raise ValueError("units must be 'fraction' or 'percent'")

        if fraction_units == units.FractionUnits.Fraction:
            if moisture_one_hour > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")
            if moisture_ten_hour > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")
            if moisture_hundred_hour > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")
            if moisture_live_woody > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")
            if moisture_live_herbaceous > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")
            if foliar_moisture > 3:
                raise ValueError("Expected moisture as fraction between 0 and 1")

        self.moisture_one_hour = moisture_one_hour
        self.moisture_ten_hour = moisture_ten_hour
        self.moisture_hundred_hour = moisture_hundred_hour
        self.moisture_live_herbaceous = moisture_live_herbaceous
        self.moisture_live_woody = moisture_live_woody
        self.foliar_moisture = foliar_moisture
        self.units = fraction_units

    @classmethod
    def from_existing(
            cls,
            dead_fuel_moisture_class: Union[int, str],
            live_fuel_moisture_class: Union[int, str],
            foliar_moisture: float = 1,
            fraction_units: str = 'fraction'
    ) -> 'MoistureScenario':
        """
            Create MoistureScenario from a preset found in Scott & Burgan (2005).

            Parameters:
            -----------
            dead_fuel_moisture_class : int or str
                Dead fuel moisture scenario. Acceptable values are:
                - 1 or 'very_low'
                - 2 or 'low'
                - 3 or 'moderate'
                - 4 or 'high'

            live_fuel_moisture_class : int or str
                Live fuel moisture scenario. Acceptable values are:
                - 1 or 'very_low'
                - 2 or 'low'
                - 3 or 'moderate'
                - 4 or 'high'

            foliar_moisture : float, optional
                The foliar moisture content, default is 1.

            fraction_units : str, optional
                The units for fraction values. Can be 'fraction' or 'percent', but fraction is recommended.

            Returns:
            --------
            instance : MoistureScenario

            Raises:
            -------
            ValueError
                If either `dead_fuel_moisture_class` or `live_fuel_moisture_class` is not one of
                the accepted values (1, 2, 3, 4 or 'very_low', 'low', 'moderate', 'high').

            Fuel Moisture Settings:
            -----------------------
            Preset values for the given classes are:

            For `dead_fuel_moisture_class`:
            - 'very_low' or 1:
                - `one_hr` = 0.03
                - `ten_hr` = 0.04
                - `hundred_hr` = 0.05
            - 'low' or 2:
                - `one_hr` = 0.06
                - `ten_hr` = 0.07
                - `hundred_hr` = 0.08
            - 'moderate' or 3:
                - `one_hr` = 0.09
                - `ten_hr` = 0.1
                - `hundred_hr` = 0.11
            - 'high' or 4:
                - `one_hr` = 0.12
                - `ten_hr` = 0.13
                - `hundred_hr` = 0.14

            For `live_fuel_moisture_class`:
            - 'very_low' or 1:
                - `live_herb` = 0.3
                - `live_woody` = 0.6
            - 'low' or 2:
                - `live_herb` = 0.6
                - `live_woody` = 0.9
            - 'moderate' or 3:
                - `live_herb` = 0.9
                - `live_woody` = 1.2
            - 'high' or 4:
                - `live_herb` = 1.2
                - `live_woody` = 1.5

            Example Usage:
            --------------
            >>> instance = MyClass.from_existing(1, 2)
            >>> instance = MyClass.from_existing('very_low', 'low')

            """

        if dead_fuel_moisture_class == 1 or dead_fuel_moisture_class=='very_low':
            one_hr = .03
            ten_hr = .04
            hundred_hr = .05
        elif dead_fuel_moisture_class == 2 or dead_fuel_moisture_class=='low':
            one_hr = .06
            ten_hr = .07
            hundred_hr = .08
        elif dead_fuel_moisture_class == 3 or dead_fuel_moisture_class=='moderate':
            one_hr = .09
            ten_hr = .1
            hundred_hr = .11
        elif dead_fuel_moisture_class == 4 or dead_fuel_moisture_class=='high':
            one_hr = .12
            ten_hr = .13
            hundred_hr = .14
        else:
            raise ValueError('dead_fuel_moisture_class must one of 1:very_low, 2:low, 3:moderate, 4:high')

        if live_fuel_moisture_class == 1 or live_fuel_moisture_class=='very_low':
            live_herb = .3
            live_woody = .6
        elif live_fuel_moisture_class == 2 or live_fuel_moisture_class=='low':
            live_herb = .6
            live_woody = .9
        elif live_fuel_moisture_class == 3 or live_fuel_moisture_class=='moderate':
            live_herb = .9
            live_woody = 1.2
        elif live_fuel_moisture_class == 4 or live_fuel_moisture_class=='high':
            live_herb = 1.2
            live_woody = 1.5
        else:
            raise ValueError('live_fuel_moisture_class must one of 1:very_low, 2:low, 3:moderate, 4:high')

        return cls(one_hr, ten_hr, hundred_hr, live_herb, live_woody, foliar_moisture, fraction_units)
