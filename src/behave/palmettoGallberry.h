/******************************************************************************
*
* Project:  CodeBlocks
* Purpose:  Class for handling the Palmetto-Gallbery special case fuel model
* Author:   William Chatham <wchatham@fs.fed.us>
* Credits:  Some of the code in the corresponding cpp file is, in part or in
*           whole, from BehavePlus5 source originally authored by Collin D.
*           Bevins and is used with or without modification.
*
*******************************************************************************
*
* THIS SOFTWARE WAS DEVELOPED AT THE ROCKY MOUNTAIN RESEARCH STATION (RMRS)
* MISSOULA FIRE SCIENCES LABORATORY BY EMPLOYEES OF THE FEDERAL GOVERNMENT
* IN THE COURSE OF THEIR OFFICIAL DUTIES. PURSUANT TO TITLE 17 SECTION 105
* OF THE UNITED STATES CODE, THIS SOFTWARE IS NOT SUBJECT TO COPYRIGHT
* PROTECTION AND IS IN THE PUBLIC DOMAIN. RMRS MISSOULA FIRE SCIENCES
* LABORATORY ASSUMES NO RESPONSIBILITY WHATSOEVER FOR ITS USE BY OTHER
* PARTIES,  AND MAKES NO GUARANTEES, EXPRESSED OR IMPLIED, ABOUT ITS QUALITY,
* RELIABILITY, OR ANY OTHER CHARACTERISTIC.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
* OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
* THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.
*
******************************************************************************/

#ifndef PALMETTOGALLBERRY_H
#define PALMETTOGALLBERRY_H

class PalmettoGallberry
{
public:
    PalmettoGallberry();
    void initializeMembers();

    double calculatePalmettoGallberyDeadFineFuelLoad(double ageOfRough, double heightOfUnderstory);
    double calculatePalmettoGallberyDeadMediumFuelLoad(double ageOfRough, double palmettoCoverage);
    double calculatePalmettoGallberyDeadFoliageLoad(double ageOfRough, double palmettoCoverage);
    double calculatePalmettoGallberyLitterLoad(double ageOfRough, double overstoryBasalArea);
    double calculatePalmettoGallberyLiveFineFuelLoad(double ageOfRough, double heightOfUnderstory);
    double calculatePalmettoGallberyLiveMediumFuelLoad(double ageOfRough, double heightOfUnderstory);
    double calculatePalmettoGallberyLiveFoliageLoad(double ageOfRough, double palmettoCoverage, double heightOfUnderstory);
    double calculatePalmettoGallberyFuelBedDepth(double heightOfUnderstory);

    double getMoistureOfExtinctionDead() const;
    double getHeatOfCombustionDead() const;
    double getHeatOfCombustionLive() const;
    double getPalmettoGallberyDeadFineFuelLoad() const;
    double getPalmettoGallberyDeadMediumFuelLoad() const;
    double getPalmettoGallberyDeadFoliageLoad() const;
    double getPalmettoGallberyFuelBedDepth() const;
    double getPalmettoGallberyLitterLoad() const;
    double getPalmettoGallberyLiveFineFuelLoad() const;
    double getPalmettoGallberyLiveMediumFuelLoad() const;
    double getPalmettoGallberyLiveFoliageLoad() const;

protected:
    double moistureOfExtinctionDead_;
    double heatOfCombustionDead_;
    double heatOfCombustionLive_;
    double palmettoGallberyDeadFineFuelLoad_;
    double palmettoGallberyDeadMediumFuelLoad_;
    double palmettoGallberyDeadFoliageFuelLoad_;
    double palmettoGallberyFuelBedDepth_;
    double palmettoGallberyLitterLoad_;
    double palmettoGallberyLiveFineFuelLoad_;
    double palmettoGallberyLiveMediumFuelLoad_;
    double palmettoGallberyLiveFoliageLoad_;
};

#endif // PALMETTOGALLBERRY_H
