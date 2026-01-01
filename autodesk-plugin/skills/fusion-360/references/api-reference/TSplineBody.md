# TSplineBody Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/TSpline/TSplineBody.h>

## Description

A TSpline body.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](TSplineBody_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getTSMDescription](TSplineBody_getTSMDescription.htm) | Returns the T-Spline body as a string in the form of a TSM description. |
| [saveAsTSMFile](TSplineBody_saveAsTSMFile.htm) | Saves the body as a TSM file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [entityToken](TSplineBody_entityToken.htm) | Returns a token for the TSplineBody object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same T-Spline body. |
| [isValid](TSplineBody_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](TSplineBody_name.htm) | Gets and sets the name of the body. If setting this property, there is the side-effect that the B-Rep body created from this T-Spline body is also renamed. |
| [objectType](TSplineBody_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentFormFeature](TSplineBody_parentFormFeature.htm) | Returns the owning form feature. |
| [textureMapControl](TSplineBody_textureMapControl.htm) | Returns the TextureMapControl object associated with this body when there is an appearance assigned to the body that has a texture associated with it. If there isn't a texture, this property will return null. If there is a texture, you can use the returned object to query and modify how the texture is applied to the body. |

## Accessed From

[TSplineBodies.addByTSMDescription](TSplineBodies_addByTSMDescription.htm), [TSplineBodies.addByTSMFile](TSplineBodies_addByTSMFile.htm), [TSplineBodies.item](TSplineBodies_item.htm), [TSplineBodies.itemByName](TSplineBodies_itemByName.htm)

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |