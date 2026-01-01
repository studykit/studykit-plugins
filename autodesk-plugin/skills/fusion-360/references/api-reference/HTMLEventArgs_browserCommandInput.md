# HTMLEventArgs.browserCommandInput Property

Parent Object: [HTMLEventArgs](HTMLEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/HTMLEventArgs.h>

## Description

When the event is fired from a BrowserCommandInput object, this property returns the specific BrowserCommandInput that caused the event to fire. In all other cases this property returns null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. |

"hTMLEventArgs\_var" is a variable referencing a HTMLEventArgs object. ```` ``` #include <Core/UserInterface/HTMLEventArgs.h>  // Get the value of the property. Ptr<BrowserCommandInput> propertyValue = hTMLEventArgs_var->browserCommandInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [BrowserCommandInput](BrowserCommandInput.htm).

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |