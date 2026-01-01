# ChainSelection.isOpenAllowed Property

Parent Object: [ChainSelection](ChainSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/ChainSelection.h>

## Description

Property to specify if the underlying CadContours2DParameterValue allows open contours. Some examples of some open contours are adaptive clearing 3d and swarf. And, some examples of closed contours are face and machining boundary.

## Syntax

* [Python](#Python)
* [C++](#C++)

"chainSelection\_var" is a variable referencing a ChainSelection object. |

"chainSelection\_var" is a variable referencing a ChainSelection object. ```` ``` #include <Cam/GeometrySelections/ChainSelection.h>  // Get the value of the property. boolean propertyValue = chainSelection_var->isOpenAllowed(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |