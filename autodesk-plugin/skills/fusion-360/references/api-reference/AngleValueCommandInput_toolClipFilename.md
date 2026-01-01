# AngleValueCommandInput.toolClipFilename Property

Parent Object: [AngleValueCommandInput](AngleValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/AngleValueCommandInput.h>

## Description

Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. |

"angleValueCommandInput\_var" is a variable referencing an AngleValueCommandInput object. ```` ``` #include <Core/UserInterface/AngleValueCommandInput.h>  // Get the value of the property. string propertyValue = angleValueCommandInput_var->toolClipFilename();  // Set the value of the property, where value_var is a string. bool returnValue = angleValueCommandInput_var->toolClipFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |