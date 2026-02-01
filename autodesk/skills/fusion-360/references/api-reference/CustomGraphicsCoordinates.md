# CustomGraphicsCoordinates Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsCoordinates.h>

## Description

Represents coordinates that are used to define vertices in custom graphics.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomGraphicsCoordinates_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](CustomGraphicsCoordinates_create.htm) | Static method that creates a CustomGraphicsCoordinates object which can be used as input to various custom graphics methods. |
| [getColor](CustomGraphicsCoordinates_getColor.htm) | Gets the color assigned to the coordinate at the specified index. |
| [getCoordinate](CustomGraphicsCoordinates_getCoordinate.htm) | Gets the coordinate at the specified index. |
| [setColor](CustomGraphicsCoordinates_setColor.htm) | Sets the color of the coordinate at the specified index. |
| [setCoordinate](CustomGraphicsCoordinates_setCoordinate.htm) | Sets the coordinate at the specified index. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [colors](CustomGraphicsCoordinates_colors.htm) | Gets and sets the colors associated with the coordinate data. This is used when a mesh is displayed using per-vertex coloring. The color at each vertex is represented by four values where they are the red, green, blue, and alpha values. This should contain the same number of colors as vertices. |
| [coordinateCount](CustomGraphicsCoordinates_coordinateCount.htm) | Returns the number of coordinates defined in the CustomGraphicsCoordinates object. |
| [coordinates](CustomGraphicsCoordinates_coordinates.htm) | Gets and sets the coordinate data associated with this CustomGraphicsCoordinates object. This data represents the x, y, z components of the coordinates where the unit of measure is centimeters. |
| [isValid](CustomGraphicsCoordinates_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomGraphicsCoordinates_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomGraphicsCoordinates.create](CustomGraphicsCoordinates_create.htm), [CustomGraphicsLines.coordinates](CustomGraphicsLines_coordinates.htm), [CustomGraphicsMesh.coordinates](CustomGraphicsMesh_coordinates.htm), [CustomGraphicsPointSet.coordinates](CustomGraphicsPointSet_coordinates.htm)

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |