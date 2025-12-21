# HemDefinition Object

## Description

The HemDefinition object represents all of the information that defines a hem feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../HemDefinition/HemDefinition_Copy.md) | Method that creates a copy of this HemDefinition object. |
| [SetCenteredWidthExtent](../HemDefinition/HemDefinition_SetCenteredWidthExtent.md) | Method that changes the HemDefinition object to define a hem that's centered along the edge and has a defined width. |
| [SetDoubleHemType](../HemDefinition/HemDefinition_SetDoubleHemType.md) | Method that changes the HemDefinition object to define a hem whose shape has a double bend. |
| [SetEdgeWidthExtent](../HemDefinition/HemDefinition_SetEdgeWidthExtent.md) | Method that changes the ContourFlangeDefinition object to define a hem whose width is defined by the length of the input edge(s). These are the same edges that were specified to define the location of the hems. |
| [SetFromToWidthExtent](../HemDefinition/HemDefinition_SetFromToWidthExtent.md) | Method that changes the FlangeDefinition object to define a hem whose width is defined as being between two entities. |
| [SetOffsetWidthExtent](../HemDefinition/HemDefinition_SetOffsetWidthExtent.md) | Method that changes the HemDefinition object to define a hem whose width is defined with respect to two entities. |
| [SetRolledHemType](../HemDefinition/HemDefinition_SetRolledHemType.md) | Method that changes the HemDefinition object to define a hem whose shape has a rolled bend. |
| [SetSingleHemType](../HemDefinition/HemDefinition_SetSingleHemType.md) | Method that changes the HemDefinition object to define a hem whose shape has a single bend. |
| [SetTeardropHemType](../HemDefinition/HemDefinition_SetTeardropHemType.md) | Method that changes the HemDefinition object to define a hem whose shape has a teardrop bend. |
| [SetWidthOffsetWidthExtent](../HemDefinition/HemDefinition_SetWidthOffsetWidthExtent.md) | Method that changes the ContourFlangeDefinition object to define a hem whose width is defined relative to another entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HemDefinition/HemDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BendOptions](../HemDefinition/HemDefinition_BendOptions.md) | Gets and sets the bend options associated with this contour flange feature. |
| [Edges](../HemDefinition/HemDefinition_Edges.md) | Gets and sets the EdgeCollection object that contains the edges that are used to define the hem feature. |
| [HemType](../HemDefinition/HemDefinition_HemType.md) | Property that returns the method used to define the type of hem. |
| [HemTypeDefinition](../HemDefinition/HemDefinition_HemTypeDefinition.md) | Property that returns the HemTypeDefinition object that defines the type of hem. |
| [IsOnEdgeSide](../HemDefinition/HemDefinition_IsOnEdgeSide.md) | Gets and sets the side of the part that the hem is on. |
| [IsUnfoldMethodOverridden](../HemDefinition/HemDefinition_IsUnfoldMethodOverridden.md) | Read-write property that gets and set whether the unfold method has been overridden for this feature. Setting this property to False clears the override. Setting the property to True returns a failure. |
| [Parent](../HemDefinition/HemDefinition_Parent.md) | Property that returns the parent HemFeature of this HemDefinition object. |
| [Type](../HemDefinition/HemDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UnfoldMethod](../HemDefinition/HemDefinition_UnfoldMethod.md) | Gets and sets the UnfoldMethod object that defines how the bends associated with this contour flange feature are unfolded. |
| [WidthExtent](../HemDefinition/HemDefinition_WidthExtent.md) | Property that returns the PartFeatureExtent object that defines how the width extent of the hem feature is defined. |
| [WidthExtentType](../HemDefinition/HemDefinition_WidthExtentType.md) | Property that returns the method used to define the width extent. |

## Accessed From

[DoubleHemDefinition.Parent](../DoubleHemDefinition/DoubleHemDefinition_Parent.md), [HemDefinition.Copy](../HemDefinition/HemDefinition_Copy.md), [HemFeature.Definition](../HemFeature/HemFeature_Definition.md), [HemFeatureProxy.Definition](../HemFeatureProxy/HemFeatureProxy_Definition.md), [HemFeatures.CreateHemDefinition](../HemFeatures/HemFeatures_CreateHemDefinition.md), [RolledHemDefinition.Parent](../RolledHemDefinition/RolledHemDefinition_Parent.md), [SingleHemDefinition.Parent](../SingleHemDefinition/SingleHemDefinition_Parent.md), [TeardropHemDefinition.Parent](../TeardropHemDefinition/TeardropHemDefinition_Parent.md)

## Version

Introduced in version 2009
