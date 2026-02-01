# SketchOptions Object

## Description

The SketchOptions object provides access to properties that provide read and write access of the 2D sketch related application options. This is somewhat equivalent to the 2D Sketch portion on the Sketch tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchOptions/SketchOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AutoBendWithLineCreation](../SketchOptions/SketchOptions_AutoBendWithLineCreation.md) | Enables/disables automatically creating corner bends on 3D lines. |
| [AutomaticReferenceEdges](../SketchOptions/SketchOptions_AutomaticReferenceEdges.md) | Gets/sets the capability to automatically project edges of the selected face onto the sketch plane as reference geometry, when creating a new sketch. |
| [AutoProjectEdges](../SketchOptions/SketchOptions_AutoProjectEdges.md) | Gets/sets the capability to select and project existing geometry to the current sketch by rubbing existing lines. |
| [AutoProjectPartOrigin](../SketchOptions/SketchOptions_AutoProjectPartOrigin.md) | Enables/disables projecting the part origin onto a sketch when the sketch is created. |
| [AutoScaleSketchGeometriesOnInitialDimension](../SketchOptions/SketchOptions_AutoScaleSketchGeometriesOnInitialDimension.md) | Enables/disables whether to auto scale sketch geometries on initial dimension. |
| [ConstraintToolbarScale](../SketchOptions/SketchOptions_ConstraintToolbarScale.md) | Gets/sets the scale for the size of the constraint toolbars with respect to the graphics window. |
| [DisplayAxes](../SketchOptions/SketchOptions_DisplayAxes.md) | Enables/disables the display of the sketch plane axes. |
| [DisplayCoordinateSystemIndicator](../SketchOptions/SketchOptions_DisplayCoordinateSystemIndicator.md) | Enables/disables the display of the sketch plane coordinate system indicator (triad). |
| [DisplayGridLines](../SketchOptions/SketchOptions_DisplayGridLines.md) | Enables/disables the display of the sketch plane grid lines. |
| [DisplayMinorGridLines](../SketchOptions/SketchOptions_DisplayMinorGridLines.md) | Enables/disables the display of minor sketch plane grid lines. |
| [HeadsUpDisplayOptions](../SketchOptions/SketchOptions_HeadsUpDisplayOptions.md) | Property that returns the HeadsUpDisplayOptions object. The HeadsUpDisplayOptions object provides access to various heads-up display related application level options for sketches. |
| [ImageInsertionLINKOptionCheckedAsDefault](../SketchOptions/SketchOptions_ImageInsertionLINKOptionCheckedAsDefault.md) | Gets/sets the default option for LINK when attaching image. |
| [ParallelViewOnSketchCreationInAssembly](../SketchOptions/SketchOptions_ParallelViewOnSketchCreationInAssembly.md) | Enables/disables whether the view is automatically reoriented to be planar to the screen in assembly environment. |
| [ParallelViewOnSketchCreationInPart](../SketchOptions/SketchOptions_ParallelViewOnSketchCreationInPart.md) | Enables/disables whether the view is automatically reoriented to be planar to the screen in part environment. |
| [PointAlignment](../SketchOptions/SketchOptions_PointAlignment.md) | Gets/sets whether to infer alignment between endpoints of newly created geometry and points of existing geometry. |
| [ProjectObjectsAsConstructionGeometry](../SketchOptions/SketchOptions_ProjectObjectsAsConstructionGeometry.md) | Enables/disables whether project objects as construction geometry. |
| [SketchConstraintSettings](../SketchOptions/SketchOptions_SketchConstraintSettings.md) | Returns the SketchConstraintSettings object. |
| [SketchOpacity](../SketchOptions/SketchOptions_SketchOpacity.md) | Gets/sets the opacity of the sketch displayed through shaded model, valid value is from 0 to 100 indicating the opacity percentage. |
| [SnapToGrid](../SketchOptions/SketchOptions_SnapToGrid.md) | Enables/disables the snap behavior for sketching tasks. |
| [SplineDefaultTension](../SketchOptions/SketchOptions_SplineDefaultTension.md) | Gets/sets the default tension for splines in 2d sketches. |
| [SplineFitMethod](../SketchOptions/SketchOptions_SplineFitMethod.md) | Gets/sets the default fit method for splines in 2d sketches. |
| [Type](../SketchOptions/SketchOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.SketchOptions](../Application/Application_SketchOptions.md), [HeadsUpDisplayOptions.Parent](../HeadsUpDisplayOptions/HeadsUpDisplayOptions_Parent.md), [InventorServer.SketchOptions](InventorServer_SketchOptions.md), [InventorServerObject.SketchOptions](InventorServerObject_SketchOptions.md), [SketchConstraintSettings.Parent](../SketchConstraintSettings/SketchConstraintSettings_Parent.md)

## Version

Introduced in version 9
