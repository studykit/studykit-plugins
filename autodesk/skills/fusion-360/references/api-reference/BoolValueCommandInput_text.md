# BoolValueCommandInput.text Property

Parent Object: [BoolValueCommandInput](BoolValueCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BoolValueCommandInput.h>

## Description

Gets and sets text to be displayed on the button. If the resourceFolder is not specified then the button will be displayed with only text. If text and the resource folder are specified then both the icon and text will be displayed.

## Syntax

* [Python](#Python)
* [C++](#C++)

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. |

"boolValueCommandInput\_var" is a variable referencing a BoolValueCommandInput object. ```` ``` #include <Core/UserInterface/BoolValueCommandInput.h>  // Get the value of the property. string propertyValue = boolValueCommandInput_var->text();  // Set the value of the property, where value_var is a string. bool returnValue = boolValueCommandInput_var->text(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |