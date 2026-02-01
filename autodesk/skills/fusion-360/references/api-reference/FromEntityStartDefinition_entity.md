# FromEntityStartDefinition.entity Property

Parent Object: [FromEntityStartDefinition](FromEntityStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FromEntityStartDefinition.h>

## Description

Gets and sets the entity defining the start of the feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. |

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. ```` ``` #include <Fusion/Features/FromEntityStartDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = fromEntityStartDefinition_var->entity();  // Set the value of the property, where value_var is a Base. bool returnValue = fromEntityStartDefinition_var->entity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |