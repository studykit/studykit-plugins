# Application.isComponentColorsDisplayed Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Get and sets if component colors are used when displaying the components within a design. This is the API equivalent of the "Display Component Colors" command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. boolean propertyValue = application_var->isComponentColorsDisplayed();  // Set the value of the property, where value_var is a boolean. bool returnValue = application_var->isComponentColorsDisplayed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |