# DocumentEventArgs.firingEvent Property

Parent Object: [DocumentEventArgs](DocumentEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. |

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. ```` ``` #include <Core/Application/DocumentEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = documentEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |