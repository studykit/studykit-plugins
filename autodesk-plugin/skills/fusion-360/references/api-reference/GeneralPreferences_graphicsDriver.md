# GeneralPreferences.graphicsDriver Property

Parent Object: [GeneralPreferences](GeneralPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GeneralPreferences.h>

## Description

Gets and sets the graphics driver used to display the graphics.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. |

"generalPreferences\_var" is a variable referencing a GeneralPreferences object. ```` ``` #include <Core/Application/GeneralPreferences.h>  // Get the value of the property. GraphicsDrivers propertyValue = generalPreferences_var->graphicsDriver();  // Set the value of the property, where value_var is a GraphicsDrivers. bool returnValue = generalPreferences_var->graphicsDriver(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [GraphicsDrivers](GraphicsDrivers.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |