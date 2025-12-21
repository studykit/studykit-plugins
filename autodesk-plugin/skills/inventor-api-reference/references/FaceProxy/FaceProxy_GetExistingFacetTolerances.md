# FaceProxy.GetExistingFacetTolerances Method

Parent Object: [FaceProxy](../FaceProxy/FaceProxy.md)

## Description

Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method. If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to facets. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities.

## Syntax

FaceProxy.**GetExistingFacetTolerances**( ***ToleranceCount*** As Long, ***ExistingTolerances***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceCount | Long | Output Long that specifies the number of existing facet sets. |
| ExistingTolerances | Double | Output array of Doubles that contains the tolerances that were used to compute the existing sets of display facets. |

## Version

Introduced in version 5.3
