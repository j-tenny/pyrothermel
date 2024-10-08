//------------------------------------------------------------------------------
/*! \file ContainForce.h
    \author Copyright (C) 2006 by Collin D. Bevins.
    \license This is released under the GNU Public License 2.
    \brief Collection of all ContainResources dispatched to the fire.
 */

#ifndef _CONTAINFORCE_H_INCLUDED_
#define _CONTAINFORCE_H_INCLUDED_

// Custom include files
#include "Contain.h"
#include "ContainResource.h"
#include <cstring>

namespace Sem
{

// Forward class references
class Contain;

//------------------------------------------------------------------------------
/*! \class ContainForce ContainForce.h
    \brief Collection of all ContainResources dispatched to the fire.
 */

class ContainForce
{
// Class version
    static const int containForceVersion = 1;   //!< Class version

// Public methods
public:
    // Custom constructors
    ContainForce( int maxResources=250 ) ;
    // Virtual destructor
    virtual ~ContainForce( void ) ;
    // Add ContainResource into ContainForce
    ContainResource* addResource( ContainResource* resource ) ;
    // Construct ContainResource into ContainForce
    ContainResource *addResource(
        double arrival,
        double production,
        double duration=480.,
        Sem::ContainFlank flank=Sem::LeftFlank,
        char * const desc="",
        double baseCost=0.0,
        double hourCost=0.0 );

    // Force-level access methods
    double exhausted( Sem::ContainFlank flank ) const ;
    double firstArrival( Sem::ContainFlank flank ) const ;
    double nextArrival( double after, double until, Sem::ContainFlank flank ) const ;
    double productionRate( double minutesSinceReport, Sem::ContainFlank flank ) const ;
    
    //for debug
    void   logResources(bool debug,const Contain*) const ;

    // Public access to individual ContainResources
    int     resources( void ) const ;
    double  resourceArrival( int index ) const ;
    double  resourceBaseCost( int index ) const ;
    double  resourceCost( int index, double finalTime ) const ;
    char * resourceDescription( int index ) const ;
    double  resourceDuration( int index ) const ;
    Sem::ContainFlank resourceFlank( int index ) const ;
    double  resourceHourCost( int index ) const ;
    double  resourceProduction( int index ) const ;

// Protected data
protected:
    ContainResource **m_cr;     //!< Array of pointers to ContainResources
    int     m_size;             //!< Size of m_cr
    int     m_count;            //!< Items in m_cr

friend class Contain;
};

}   // End of namespace Sem

#endif

//------------------------------------------------------------------------------
//  End of ContainForce.h
//------------------------------------------------------------------------------

