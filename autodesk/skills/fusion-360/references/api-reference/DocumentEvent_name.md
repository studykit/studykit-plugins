# DocumentEvent.name Property

Parent Object: [DocumentEvent](DocumentEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEvent.h>

## Description

The name of the event - e.g. "DocumentOpening"

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEvent\_var" is a variable referencing a DocumentEvent object. |

"documentEvent\_var" is a variable referencing a DocumentEvent object. ```` ``` #include <Core/Application/DocumentEvent.h>  // Get the value of the property. string propertyValue = documentEvent_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |