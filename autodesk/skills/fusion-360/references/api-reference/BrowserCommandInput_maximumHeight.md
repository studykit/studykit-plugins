# BrowserCommandInput.maximumHeight Property

Parent Object: [BrowserCommandInput](BrowserCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BrowserCommandInput.h>

## Description

Gets and sets the maximum height of the browser within the command dialog, in pixels. As the user resizes the dialog, the area taken up by the browser will shrink and grow to fit within the defined space. It will never shrink to be less than the minimum height or expand to be larger than the maximum height. If the content displayed within the browser does not fit within the current area, a scroll bar will appear to allow the user to scroll to see the entire browser content. The default value of zero sets no maximum height, so the browser will expand to the maximum extent available.

## Syntax

* [Python](#Python)
* [C++](#C++)

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. |

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. ```` ``` #include <Core/UserInterface/BrowserCommandInput.h>  // Get the value of the property. integer propertyValue = browserCommandInput_var->maximumHeight();  // Set the value of the property, where value_var is an integer. bool returnValue = browserCommandInput_var->maximumHeight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |