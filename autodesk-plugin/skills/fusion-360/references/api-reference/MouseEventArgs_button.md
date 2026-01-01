# MouseEventArgs.button Property

Parent Object: [MouseEventArgs](MouseEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

Gets which mouse button(s) are pressed. The returned value is bitwise and can indicate that more than one button is pressed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. |

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. ```` ``` #include <Core/UserInterface/MouseEventArgs.h>  // Get the value of the property. MouseButtons propertyValue = mouseEventArgs_var->button(); ``` ```` |

## Property Value

This is a read only property whose value is a [MouseButtons](MouseButtons.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |