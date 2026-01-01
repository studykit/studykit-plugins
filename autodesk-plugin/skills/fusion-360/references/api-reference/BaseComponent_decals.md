# BaseComponent.decals Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Returns the decals collection associated with this component. This provides access to the existing decals and supports the creation of new decals.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<Decals> propertyValue = baseComponent_var->decals(); ``` ```` |

## Property Value

This is a read only property whose value is a [Decals](Decals.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |