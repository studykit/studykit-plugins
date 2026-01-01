# NetworkPreferences.networkProxySetting Property

Parent Object: [NetworkPreferences](NetworkPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NetworkPreferences.h>

## Description

Gets and sets the network proxy setting.

## Syntax

* [Python](#Python)
* [C++](#C++)

"networkPreferences\_var" is a variable referencing a NetworkPreferences object. |

"networkPreferences\_var" is a variable referencing a NetworkPreferences object. ```` ``` #include <Core/Application/NetworkPreferences.h>  // Get the value of the property. NetworkProxySettings propertyValue = networkPreferences_var->networkProxySetting();  // Set the value of the property, where value_var is a NetworkProxySettings. bool returnValue = networkPreferences_var->networkProxySetting(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [NetworkProxySettings](NetworkProxySettings.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |