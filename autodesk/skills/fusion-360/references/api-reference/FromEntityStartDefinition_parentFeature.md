# FromEntityStartDefinition.parentFeature Property

Parent Object: [FromEntityStartDefinition](FromEntityStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FromEntityStartDefinition.h>

## Description

Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. |

"fromEntityStartDefinition\_var" is a variable referencing a FromEntityStartDefinition object. ```` ``` #include <Fusion/Features/FromEntityStartDefinition.h>  // Get the value of the property. Ptr<Feature> propertyValue = fromEntityStartDefinition_var->parentFeature(); ``` ```` |

## Property Value

This is a read only property whose value is a [Feature](Feature.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |