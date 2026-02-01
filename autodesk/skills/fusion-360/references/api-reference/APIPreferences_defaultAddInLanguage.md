# APIPreferences.defaultAddInLanguage Property

Parent Object: [APIPreferences](APIPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/APIPreferences.h>

## Description

Gets and sets the preference that controls which programming language should be used when creating a new add-in. One option is to prompt the user.

## Syntax

* [Python](#Python)
* [C++](#C++)

"aPIPreferences\_var" is a variable referencing an APIPreferences object. |

"aPIPreferences\_var" is a variable referencing an APIPreferences object. ```` ``` #include <Core/Application/APIPreferences.h>  // Get the value of the property. ProgrammingLanguages propertyValue = aPIPreferences_var->defaultAddInLanguage();  // Set the value of the property, where value_var is a ProgrammingLanguages. bool returnValue = aPIPreferences_var->defaultAddInLanguage(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ProgrammingLanguages](ProgrammingLanguages.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |