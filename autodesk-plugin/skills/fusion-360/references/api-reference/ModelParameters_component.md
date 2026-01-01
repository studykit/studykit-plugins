# ModelParameters.component Property

Parent Object: [ModelParameters](ModelParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameters.h>

## Description

Returns the component that owns the Model Parameters collection

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameters\_var" is a variable referencing a ModelParameters object. |

"modelParameters\_var" is a variable referencing a ModelParameters object. ```` ``` #include <Fusion/Fusion/ModelParameters.h>  // Get the value of the property. Ptr<Component> propertyValue = modelParameters_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |