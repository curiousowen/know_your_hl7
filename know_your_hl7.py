import hl7apy

def know_your_hl7(msh_3, msh_4, msh_5, msh_6, pid_3, pid_5, pv1_1, pv1_2, nk1_2, obx_1, obx_2, obx_3, obx_5, nte_1, nte_3, al1_2):
    """
    Generates an HL7 message with specified segments and fields.

    Parameters:
    - msh_3: Sending Application
    - msh_4: Sending Facility
    - msh_5: Receiving Application
    - msh_6: Receiving Facility
    - pid_3: Patient ID
    - pid_5: Patient Name (Last^First^Middle^^Mr.)
    - pv1_1: Patient Class (e.g., O = Outpatient)
    - pv1_2: Patient Type (e.g., OP^Outpatient)
    - nk1_2: Next of Kin (e.g., Mother^Next)
    - obx_1: Set ID - OBX
    - obx_2: Value Type (e.g., NM = Numeric)
    - obx_3: Observation Identifier (e.g., Weight)
    - obx_5: Observation Value (e.g., 70)
    - nte_1: Set ID - NTE
    - nte_3: Comment (e.g., Additional comments)
    - al1_2: Allergy Type (e.g., Pollen)

    Returns:
    - hl7apy.Message: Generated HL7 message object
    """
    # Create an HL7 message
    message = hl7apy.Message("ADT_A01")

    # MSH Segment
    message.msh.msh_3 = msh_3
    message.msh.msh_4 = msh_4
    message.msh.msh_5 = msh_5
    message.msh.msh_6 = msh_6

    # PID Segment
    pid = message.add_segment()
    pid.pid_3 = pid_3
    pid.pid_5 = pid_5

    # PV1 Segment
    pv1 = message.add_segment()
    pv1.pv1_1 = pv1_1
    pv1.pv1_2 = pv1_2

    # NK1 Segment
    nk1 = message.add_segment()
    nk1.nk1_2 = nk1_2

    # OBX Segment
    obx = message.add_segment()
    obx.obx_1 = obx_1
    obx.obx_2 = obx_2
    obx.obx_3 = obx_3
    obx.obx_5 = obx_5

    # NTE Segment
    nte = message.add_segment()
    nte.nte_1 = nte_1
    nte.nte_3 = nte_3

    # AL1 Segment
    al1 = message.add_segment()
    al1.al1_2 = al1_2

    return message

if __name__ == "__main__":
    # Example usage
    print("Welcome to HL7 Message Generator!")
    print("Please provide the following details to generate an HL7 message:")

    msh_3 = input("Sending Application (MSH-3): ")
    msh_4 = input("Sending Facility (MSH-4): ")
    msh_5 = input("Receiving Application (MSH-5): ")
    msh_6 = input("Receiving Facility (MSH-6): ")
    pid_3 = input("Patient ID (PID-3): ")
    pid_5 = input("Patient Name (Last^First^Middle^^Mr.) (PID-5): ")
    pv1_1 = input("Patient Class (e.g., O = Outpatient) (PV1-1): ")
    pv1_2 = input("Patient Type (e.g., OP^Outpatient) (PV1-2): ")
    nk1_2 = input("Next of Kin (e.g., Mother^Next) (NK1-2): ")
    obx_1 = input("Set ID - OBX (OBX-1): ")
    obx_2 = input("Value Type (e.g., NM = Numeric) (OBX-2): ")
    obx_3 = input("Observation Identifier (e.g., Weight) (OBX-3): ")
    obx_5 = input("Observation Value (e.g., 70) (OBX-5): ")
    nte_1 = input("Set ID - NTE (NTE-1): ")
    nte_3 = input("Comment (e.g., Additional comments) (NTE-3): ")
    al1_2 = input("Allergy Type (e.g., Pollen) (AL1-2): ")

    hl7_msg = know_your_hl7(msh_3, msh_4, msh_5, msh_6, pid_3, pid_5, pv1_1, pv1_2, nk1_2, obx_1, obx_2, obx_3, obx_5, nte_1, nte_3, al1_2)
    print("\nGenerated HL7 message:")
    print(hl7_msg.value)
