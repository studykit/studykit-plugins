# UnitVector Object

## Description

The UnitVector object. For more information, see the
[Transient Geometry](TransientGeometry_Overview.md) overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AngleTo](../UnitVector/UnitVector_AngleTo.md) | Determines the angle between this vector and the specified vector. |
| [AsVector](../UnitVector/UnitVector_AsVector.md) | Get the vector equivalent of this unit vector. |
| [Copy](../UnitVector/UnitVector_Copy.md) | Creates a copy of this UnitVector object. The result is entirely independent and can be edited without affecting the original UnitVector object. |
| [CrossProduct](../UnitVector/UnitVector_CrossProduct.md) | Determine the cross product between this vector and the specified vector. |
| [DotProduct](../UnitVector/UnitVector_DotProduct.md) | Determine the dot product of this vector to the specified vector. |
| [GetUnitVectorData](../UnitVector/UnitVector_GetUnitVectorData.md) | Get the data defining this unit vector. |
| [IsEqualTo](../UnitVector/UnitVector_IsEqualTo.md) | Compare this unit vector for equality to the specified unit vector. |
| [IsParallelTo](../UnitVector/UnitVector_IsParallelTo.md) | Determine if this vector is parallel to the specified vector. |
| [IsPerpendicularTo](../UnitVector/UnitVector_IsPerpendicularTo.md) | Determine if this vector is perpendicular to the specified vector. |
| [PutUnitVectorData](../UnitVector/UnitVector_PutUnitVectorData.md) | Method that sets the data defining this unit vector. |
| [TransformBy](../UnitVector/UnitVector_TransformBy.md) | Transform this vector by the specified matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [X](../UnitVector/UnitVector_X.md) | Specifies the X coordinate of the vector. If not supplied, the X value will default to 0. |
| [Y](../UnitVector/UnitVector_Y.md) | Specifies the Y coordinate of the vector. If not supplied, the Y value will default to 0. |
| [Z](../UnitVector/UnitVector_Z.md) | Specifies the Z coordinate of the vector. If not supplied, the Z value will default to 1. |

## Accessed From

[Arc3d.Normal](../Arc3d/Arc3d_Normal.md), [Arc3d.ReferenceVector](../Arc3d/Arc3d_ReferenceVector.md), [AssemblyWorkAxisDef.Axis](../AssemblyWorkAxisDef/AssemblyWorkAxisDef_Axis.md), [AssemblyWorkAxisDef.GetData](../AssemblyWorkAxisDef/AssemblyWorkAxisDef_GetData.md), [AssemblyWorkPlaneDef.GetData](../AssemblyWorkPlaneDef/AssemblyWorkPlaneDef_GetData.md), [AssemblyWorkPlaneDef.XAxis](../AssemblyWorkPlaneDef/AssemblyWorkPlaneDef_XAxis.md), [AssemblyWorkPlaneDef.YAxis](../AssemblyWorkPlaneDef/AssemblyWorkPlaneDef_YAxis.md), [BIMCableTrayConnectorDefinition.Direction](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_Direction.md), [BIMCableTrayConnectorDefinition.HeightDirection](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_HeightDirection.md), [BIMCableTrayConnectorDefinition.WidthDirection](../BIMCableTrayConnectorDefinition/BIMCableTrayConnectorDefinition_WidthDirection.md), [BIMConduitConnectorDefinition.Direction](../BIMConduitConnectorDefinition/BIMConduitConnectorDefinition_Direction.md), [BIMConnectorDefinition.Direction](../BIMConnectorDefinition/BIMConnectorDefinition_Direction.md), [BIMDuctConnectorDefinition.Direction](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_Direction.md), [BIMDuctConnectorDefinition.HeightDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_HeightDirection.md), [BIMDuctConnectorDefinition.WidthDirection](../BIMDuctConnectorDefinition/BIMDuctConnectorDefinition_WidthDirection.md), [BIMElectricalConnectorDefinition.Direction](../BIMElectricalConnectorDefinition/BIMElectricalConnectorDefinition_Direction.md), [BIMPipeConnectorDefinition.Direction](../BIMPipeConnectorDefinition/BIMPipeConnectorDefinition_Direction.md), [Camera.UpVector](../Camera/Camera_UpVector.md), [Circle.Normal](../Circle/Circle_Normal.md), [Cone.AxisVector](../Cone/Cone_AxisVector.md), [CoreCavityDefinition.PullDirection](CoreCavityDefinition_PullDirection.md), [Cylinder.AxisVector](../Cylinder/Cylinder_AxisVector.md), [DWGArc.Normal](../DWGArc/DWGArc_Normal.md), [DWGArcProxy.Normal](../DWGArcProxy/DWGArcProxy_Normal.md), [DWGEllipticalArc.Normal](../DWGEllipticalArc/DWGEllipticalArc_Normal.md), [DWGEllipticalArcProxy.Normal](../DWGEllipticalArcProxy/DWGEllipticalArcProxy_Normal.md), [DWGLine.Direction](../DWGLine/DWGLine_Direction.md), [DWGLineProxy.Direction](../DWGLineProxy/DWGLineProxy_Direction.md), [EllipseFull.Normal](../EllipseFull/EllipseFull_Normal.md), [EllipticalArc.MajorAxis](../EllipticalArc/EllipticalArc_MajorAxis.md), [EllipticalArc.MinorAxis](../EllipticalArc/EllipticalArc_MinorAxis.md), [EllipticalCone.AxisVector](../EllipticalCone/EllipticalCone_AxisVector.md), [EllipticalCylinder.AxisVector](../EllipticalCylinder/EllipticalCylinder_AxisVector.md), [FixedWorkAxisDef.Axis](../FixedWorkAxisDef/FixedWorkAxisDef_Axis.md), [FixedWorkAxisDef.GetData](../FixedWorkAxisDef/FixedWorkAxisDef_GetData.md), [FixedWorkPlaneDef.GetData](../FixedWorkPlaneDef/FixedWorkPlaneDef_GetData.md), [FixedWorkPlaneDef.XAxis](../FixedWorkPlaneDef/FixedWorkPlaneDef_XAxis.md), [FixedWorkPlaneDef.YAxis](../FixedWorkPlaneDef/FixedWorkPlaneDef_YAxis.md), [GraphicsNormalSet.Normal](../GraphicsNormalSet/GraphicsNormalSet_Normal.md), [GroundPlaneSettings.FrontDirection](../GroundPlaneSettings/GroundPlaneSettings_FrontDirection.md), [GroundPlaneSettings.UpDirection](../GroundPlaneSettings/GroundPlaneSettings_UpDirection.md), [Line.Direction](../Line/Line_Direction.md), [LineSegment.Direction](../LineSegment/LineSegment_Direction.md), [MoldDefinition.PullDirection](MoldDefinition_PullDirection.md), [Plane.Normal](../Plane/Plane_Normal.md), [PointCloudPlane.GetPlaneRectangle](../PointCloudPlane/PointCloudPlane_GetPlaneRectangle.md), [PointCloudPlaneProxy.GetPlaneRectangle](../PointCloudPlaneProxy/PointCloudPlaneProxy_GetPlaneRectangle.md), [PresentationTweak.GetRotationData](PresentationTweak_GetRotationData.md), [SketchEllipse3D.MajorAxisVector](../SketchEllipse3D/SketchEllipse3D_MajorAxisVector.md), [SketchEllipse3DProxy.MajorAxisVector](../SketchEllipse3DProxy/SketchEllipse3DProxy_MajorAxisVector.md), [SketchEllipticalArc3D.MajorAxisVector](../SketchEllipticalArc3D/SketchEllipticalArc3D_MajorAxisVector.md), [SketchEllipticalArc3DProxy.MajorAxisVector](../SketchEllipticalArc3DProxy/SketchEllipticalArc3DProxy_MajorAxisVector.md), [SketchSplineHandle3D.Tangent](../SketchSplineHandle3D/SketchSplineHandle3D_Tangent.md), [SketchSplineHandle3DProxy.Tangent](../SketchSplineHandle3DProxy/SketchSplineHandle3DProxy_Tangent.md), [Torus.AxisVector](../Torus/Torus_AxisVector.md), [TransientGeometry.CreateUnitVector](../TransientGeometry/TransientGeometry_CreateUnitVector.md), [UnitVector.Copy](../UnitVector/UnitVector_Copy.md), [UnitVector.CrossProduct](../UnitVector/UnitVector_CrossProduct.md), [Vector.AsUnitVector](../Vector/Vector_AsUnitVector.md), [WorkPlane.GetPosition](../WorkPlane/WorkPlane_GetPosition.md), [WorkPlaneProxy.GetPosition](../WorkPlaneProxy/WorkPlaneProxy_GetPosition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Offset a 2D sketch](../../sample-programs/Sketch_OffsetSketchEntitiesUsingDistance_Sample.md) | This sample demonstrates the creation of offsets in 2d sketches. Two ways of creating the offset are shown - one uses a distance and the other uses the input point. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |