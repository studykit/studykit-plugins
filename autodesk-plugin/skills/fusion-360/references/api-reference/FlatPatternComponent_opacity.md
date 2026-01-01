# FlatPatternComponent.opacity Property

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Gets and sets the opacity override assigned to this component. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object.  ```` ``` # Get the value of the property. propertyValue = flatPatternComponent_var.opacity  # Set the value of the property. flatPatternComponent_var.opacity = propertyValue ``` ```` |

"flatPatternComponent\_var" is a variable referencing a FlatPatternComponent object. ```` ``` #include <Fusion/SheetMetal/FlatPatternComponent.h>  // Get the value of the property. double propertyValue = flatPatternComponent_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = flatPatternComponent_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |