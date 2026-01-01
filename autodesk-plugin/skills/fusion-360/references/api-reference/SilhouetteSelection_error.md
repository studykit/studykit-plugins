# SilhouetteSelection.error Property

Parent Object: [SilhouetteSelection](SilhouetteSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SilhouetteSelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. |

"silhouetteSelection\_var" is a variable referencing a SilhouetteSelection object. ```` ``` #include <Cam/GeometrySelections/SilhouetteSelection.h>  // Get the value of the property. string propertyValue = silhouetteSelection_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |