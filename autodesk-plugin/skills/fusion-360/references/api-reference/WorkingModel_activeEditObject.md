# WorkingModel.activeEditObject Property

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Returns the current edit target as seen in the user interface. This edit target is defined as the container object that will be added to if something is created. For example, a component can be an edit target so that when new bodies are created they are added to that component. A sketch can also be an edit target.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a WorkingModel object. |

"workingModel\_var" is a variable referencing a WorkingModel object. ```` ``` #include <Fusion/Fusion/WorkingModel.h>  // Get the value of the property. Ptr<Base> propertyValue = workingModel_var->activeEditObject(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |