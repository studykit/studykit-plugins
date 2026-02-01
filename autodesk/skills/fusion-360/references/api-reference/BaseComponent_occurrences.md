# BaseComponent.occurrences Property

Parent Object: [BaseComponent](BaseComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/BaseComponent.h>

## Description

Property that returns the Occurrences collection associated with this component. This provides access to the occurrences at the top-level of this component and provides the functionality to add new occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"baseComponent\_var" is a variable referencing a BaseComponent object. |

"baseComponent\_var" is a variable referencing a BaseComponent object. ```` ``` #include <Fusion/Components/BaseComponent.h>  // Get the value of the property. Ptr<Occurrences> propertyValue = baseComponent_var->occurrences(); ``` ```` |

## Property Value

This is a read only property whose value is an [Occurrences](Occurrences.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |