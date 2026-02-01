# SilhouetteSelection.isValid Property

Parent Object: [SilhouetteSelection](SilhouetteSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SilhouetteSelection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. |

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. ```` ``` #include <Cam/GeometrySelections/SilhouetteSelection.h>  // Get the value of the property. boolean propertyValue = silhouetteSelection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |