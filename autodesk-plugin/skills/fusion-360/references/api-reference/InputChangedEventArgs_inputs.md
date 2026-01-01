# InputChangedEventArgs.inputs Property

Parent Object: [InputChangedEventArgs](InputChangedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEventArgs.h>

## Description

Returns the collection of command inputs that are associated with the command this event is being fired for.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. |

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. ```` ``` #include <Core/UserInterface/InputChangedEventArgs.h>  // Get the value of the property. Ptr<CommandInputs> propertyValue = inputChangedEventArgs_var->inputs(); ``` ```` |

## Property Value

This is a read only property whose value is a [CommandInputs](CommandInputs.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |