# SurfaceBody.GetExistingFacetTolerances Method

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Method that gets the tolerances that were used to calculate the existing sets of display facets. These can be used to determine if any existing facets have been calculated within your desired accuracy. The tolerance value is also used as an index to specify which set of existing facets to retrieve when using the GetExistingFacets method.

## Remarks

If you are using this method within Apprentice, you can use the DisplayAffinity property to optimize Apprentice for access to facets. Setting this property to True before you begin to traverse an assembly notifies Apprentice not to load any B-rep entities. Note that CalculateFacets and GetExistingFacets (or GetExistingTolerances) are completely unrelated other than they both deal in facet data. CalculateFacets facets the model and returns that result. It does not effect any information held by Inventor. It is just direct access to the \internal facet generator. The GetExistingFacets/Tolerances methods access the existing facet data held by the internal scene, if any. They access the set of existing tolerances and facets currently being held. Therefore it is quite possible that existing facets at a given tolerance may not exactly match calculated facets at the same tolerance.

## Syntax

SurfaceBody.**GetExistingFacetTolerances**( ***ToleranceCount*** As Long, ***ExistingTolerances***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ToleranceCount | Long | Output Long that specifies the number of existing facet sets. |
| ExistingTolerances | Double | Output array of Doubles that contains the tolerances that were used to compute the existing sets of display facets. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Client Graphics - Vertex Color by Z Height](../../sample-programs/GraphicsDataSets_CreateColorSet_Sample.md) | This sample demonstrates using client graphics and some other functions that help to support display control. It uses the currently active part and replaces the part display with a display where the part's color varies from blue to red where blue is assigned to the lowest Z portion of the part and red is assigned to the highest Z portion of the part. Areas in between are represented by a smooth blend of color from blue to red. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |