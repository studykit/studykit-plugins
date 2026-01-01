# CurveSelections.createNewSilhouetteSelection Method

Parent Object: [CurveSelections](CurveSelections.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/CurveSelections.h>

## Description

Creates a new silhouette selection and adds it to the end of the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object.```` ``` returnValue = curveSelections_var.createNewSilhouetteSelection() ``` ```` |

"curveSelections\_var" is a variable referencing a [CurveSelections](CurveSelections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SilhouetteSelection](SilhouetteSelection.htm) | Returns newly created SilhouetteSelection. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Wood Routing Workflow Sample](WoodRoutingSample_Sample.htm) | This script demonstrates routing wood panels. When running the sample, it assumes you have an open design containing one or more "panels" oriented flat in the X-Y plane. The script creates a setup and a 2D contour operation with tabs to route the panels from a standard sheet. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |