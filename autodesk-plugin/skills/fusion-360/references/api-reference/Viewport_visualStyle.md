# Viewport.visualStyle Property

Parent Object: [Viewport](Viewport.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Viewport.h>

## Description

Gets and sets the current visual style being used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"viewport\_var" is a variable referencing a Viewport object. |

"viewport\_var" is a variable referencing a Viewport object. ```` ``` #include <Core/Application/Viewport.h>  // Get the value of the property. VisualStyles propertyValue = viewport_var->visualStyle();  // Set the value of the property, where value_var is a VisualStyles. bool returnValue = viewport_var->visualStyle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [VisualStyles](VisualStyles.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |