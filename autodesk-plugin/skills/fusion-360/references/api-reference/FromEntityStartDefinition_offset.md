# FromEntityStartDefinition.offset Property

Parent Object: [FromEntityStartDefinition](FromEntityStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FromEntityStartDefinition.h>

## Description

Gets the currently defined offset value. If the FromEntityStartDefinition object was created statically and is not associated with a feature, this will return a ValueInput object. if the FromEntityStartDefinition is associated with an existing feature, this will return the parameter that was created when the feature was created. To edit the offset, use properties on the parameter to change the value of the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. |

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. ```` ``` #include <Fusion/Features/FromEntityStartDefinition.h>  // Get the value of the property. Ptr<Base> propertyValue = fromEntityStartDefinition_var->offset(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |