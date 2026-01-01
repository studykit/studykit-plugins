# SilhouetteSelection.sideType Property

Parent Object: [SilhouetteSelection](SilhouetteSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SilhouetteSelection.h>

## Description

Desired side type. The default is StartOutside.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. |

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. ```` ``` #include <Cam/GeometrySelections/SilhouetteSelection.h>  // Get the value of the property. SideTypes propertyValue = silhouetteSelection_var->sideType();  // Set the value of the property, where value_var is a SideTypes. bool returnValue = silhouetteSelection_var->sideType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [SideTypes](SideTypes.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |