# SilhouetteSelection.silhouetteTolerance Property

Parent Object: [SilhouetteSelection](SilhouetteSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SilhouetteSelection.h>

## Description

The distance the silhouette can differ from the model. This helps in creating a silhouette in situations where one cannot be created because of open contours.Generally, the tolerance value you use should be smaller than or equal to the machining tolerance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. |

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. ```` ``` #include <Cam/GeometrySelections/SilhouetteSelection.h>  // Get the value of the property. double propertyValue = silhouetteSelection_var->silhouetteTolerance();  // Set the value of the property, where value_var is a double. bool returnValue = silhouetteSelection_var->silhouetteTolerance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version July 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |