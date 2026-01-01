# Play back a simulation

## Description

This sample plays back an existing dynamic simulation.

## Code Samples

* [VBA](#VBA)

To run this sample you must have an active document that has a valid simulation defined.

```
Sub PlaySimulation()
    ' Get the active document.  This assumes it is an assembly.
    Dim asmDoc As AssemblyDocument
    Set asmDoc = ThisApplication.ActiveDocument

    ' The Dynamic Simulation environment must be active.
    Dim UIManager As UserInterfaceManager
    Set UIManager = ThisApplication.UserInterfaceManager
    If UIManager.ActiveEnvironment.InternalName <> "DynamicSimulationEnvironmentInternalName" Then
        ' Get the environment manager.
        Dim environmentMgr As EnvironmentManager
        Set environmentMgr = asmDoc.EnvironmentManager

        Dim dsEnv As Environment
        Set dsEnv = UIManager.Environments.Item("DynamicSimulationEnvironmentInternalName")
        Call environmentMgr.SetCurrentEnvironment(dsEnv)
    End If

    ' Get the simulation manager from the assembly.
    Dim simManager As SimulationManager
    Set simManager = asmDoc.ComponentDefinition.SimulationManager

    ' Get the first simulation.  Currently there is only ever one.
    Dim sim As DynamicSimulation
    Set sim = simManager.DynamicSimulations.Item(1)

    ' Check to see if the simulation has already been computed.
    If sim.LastComputedTimeStep < sim.NumberOfTimeSteps Then
        ' Compute the simulation, which will also play it.
        sim.ComputeSimulation
    Else
        ' Play the computed simulation.
        sim.PlaySimulation
    End If
End Sub
```
