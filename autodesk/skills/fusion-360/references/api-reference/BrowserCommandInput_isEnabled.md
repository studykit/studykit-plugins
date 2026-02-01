# BrowserCommandInput.isEnabled Property

Parent Object: [BrowserCommandInput](BrowserCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BrowserCommandInput.h>

## Description

Gets or sets if this input is currently enabled or disabled for user interaction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object.  ```` ``` # Get the value of the property. propertyValue = browserCommandInput_var.isEnabled  # Set the value of the property. browserCommandInput_var.isEnabled = propertyValue ``` ```` |

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. ```` ``` #include <Core/UserInterface/BrowserCommandInput.h>  // Get the value of the property. boolean propertyValue = browserCommandInput_var->isEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = browserCommandInput_var->isEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |