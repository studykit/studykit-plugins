# StringValueCommandInput.toolClipFilename Property

Parent Object: [StringValueCommandInput](StringValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/StringValueCommandInput.h>

## Description

Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. |

"stringValueCommandInput\_var" is a variable referencing a StringValueCommandInput object. ```` ``` #include <Core/UserInterface/StringValueCommandInput.h>  // Get the value of the property. string propertyValue = stringValueCommandInput_var->toolClipFilename();  // Set the value of the property, where value_var is a string. bool returnValue = stringValueCommandInput_var->toolClipFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |