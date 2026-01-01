# SurfaceBodyProxy.GetExistingFacetTolerances Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method.

## Syntax

SurfaceBodyProxy.**GetExistingFacetTolerances**( ***ToleranceCount*** As Long, ***ExistingTolerances***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceCount | Long | Output Long that specifies the number of existing facet sets. |
| ExistingTolerances | Double | Output array of Doubles that contains the tolerances that were used to compute the existing sets of display facets. |

## Version

Introduced in version 5.3
