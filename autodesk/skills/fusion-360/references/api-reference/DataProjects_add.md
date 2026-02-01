# DataProjects.add Method

Parent Object: [DataProjects](DataProjects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

Creates a new project in the parent hub.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"dataProjects\_var" is a variable referencing a [DataProjects](DataProjects.htm) object.  ```` ``` #include <Core/Dashboard/DataProjects.h>  // Uses no optional arguments. returnValue = dataProjects_var->add(name);  // Uses optional arguments. returnValue = dataProjects_var->add(name, purpose, contributors); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [DataProject](DataProject.htm) | Returns the created DataProject object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the project. This is the name visible to the user. |
| purpose | string | Optional description of the purpose of the project. An empty string can be used to not specify a purpose.   This is an optional argument whose default value is "". |
| contributors | string | Optional list of contributors where the list consists of email addresses separated by a comma. An empty string can be used to not specify any contributors.   This is an optional argument whose default value is "". |

## Version

Introduced in version September 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |