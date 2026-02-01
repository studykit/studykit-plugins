# Application.supportedProductTypes Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns an array containing the names of the products types currently supported by Fusion. For example, the name returned for Fusion is "DesignProductType". These product type names are used to identify specific products in some other API functions such as the productType property on the Workspace and ToolbarPanel objects.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. std::vector<string> propertyValue = application_var->supportedProductTypes(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |