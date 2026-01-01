# Decal.isVisible Property

Parent Object: [Decal](Decal.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decal.h>

## Description

Returns if the decal is currently visible in the graphics window. The isLightBulbOn property of the decal controls if the decal should be displayed or not, but even when true, the decal may not be visible because the occurrence that references the component may not be visible. It's also possible to turn off the visibility of all the decals in a component. This property takes all of that into account when reporting if the decal is visible or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decal\_var" is a variable referencing a Decal object. |

"decal\_var" is a variable referencing a Decal object. ```` ``` #include <Fusion/Image/Decal.h>  // Get the value of the property. boolean propertyValue = decal_var->isVisible(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |