# InputChangedEventArgs.isValid Property

Parent Object: [InputChangedEventArgs](InputChangedEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/InputChangedEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. |

"inputChangedEventArgs\_var" is a variable referencing an InputChangedEventArgs object. ```` ``` #include <Core/UserInterface/InputChangedEventArgs.h>  // Get the value of the property. boolean propertyValue = inputChangedEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |