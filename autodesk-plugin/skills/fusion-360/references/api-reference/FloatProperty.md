# FloatProperty Object

Derived from: [Property](Property.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

A float or real value property.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FloatProperty_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getLimits](FloatProperty_getLimits.htm) | Method that returns any limits for the value of this property. The HasLimits property can be used to see if there are any limits or not. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [connectedTexture](FloatProperty_connectedTexture.htm) | When the property is associated with an appearance, this gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If it's parent writable you can edit the texture. If no texture exists, this property will return null. |
| [hasConnectedTexture](FloatProperty_hasConnectedTexture.htm) | When the property is associated with an appearance this indicates if the float value has been overridden using a texture. Setting this property to False will remove the texture so that a float value is used. Setting this property to True will connect a texture to this float value. For properties not associated with an appearance, this acts as read-only and always returns false. |
| [hasLimits](FloatProperty_hasLimits.htm) | Gets the boolean flag that indicates if the value of this property has any limits it must be within to be valid. If True, use the GetLimits method to get the limit values.   This is most commonly used for properties associated with materials and appearances and in most cases will return false. |
| [hasMultipleValues](FloatProperty_hasMultipleValues.htm) | Gets the boolean flag that indicates if this property has multiple values or not.   This is most commonly used for properties associated with materials and appearances. |
| [id](FloatProperty_id.htm) | Returns the unique ID of this property. |
| [isPercentage](FloatProperty_isPercentage.htm) | Gets the boolean flag that indicates that this property represents a percentage value so the valid values must be in the range of 0.0 to 1.0 unless they’re further limited by additional limits which can be determined with the HasLimits property.   This is most commonly used for properties associated with materials and appearances. |
| [isReadOnly](FloatProperty_isReadOnly.htm) | Indicates if this property is read-only. If True any attempted edits will fail. |
| [isValid](FloatProperty_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](FloatProperty_name.htm) | Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language |
| [objectType](FloatProperty_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parent](FloatProperty_parent.htm) | Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in. |
| [units](FloatProperty_units.htm) | Gets the units that the value of this property is returned in. The String returned is a valid Fusion unit string. An empty string indicates a unitless value. |
| [value](FloatProperty_value.htm) | Gets and sets this property value. The value of this property should be ignored if the HasConnectedTexture property is true. Setting this will remove any associated texture, if there is one. |
| [values](FloatProperty_values.htm) | Gets and sets the values associated with this property. HasMultipleValues property indicates if this property will be returning more than one value.   This is most commonly used for properties associated with materials and appearances. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |