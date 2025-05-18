import mysql.connector
import time

def connect_to_database():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="bd123!",
        database="bd2"
    )
    return conn

def search_patient_by_cpf(cpf):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "SELECT * FROM hospital.paciente WHERE CPF = %s"
    
    start_time = time.time()
    cursor.execute(query, (cpf,))
    result = cursor.fetchall()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da consulta: {end_time - start_time:.10f} segundos")
    return result

def search_consulta(patient_id=None, date=None, crm=None):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "SELECT * FROM hospital.consulta WHERE 1=1"
    params = []
    
    if patient_id:
        query += " AND IdPac = %s"
        params.append(patient_id)
    if date:
        query += " AND Data = %s"
        params.append(date)
    if crm:
        query += " AND CRM = %s"
        params.append(crm)
        
    start_time = time.time()
    cursor.execute(query, tuple(params))
    result = cursor.fetchall()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da consulta: {end_time - start_time:.10f} segundos")
    return result

def insert_consulta(crm, idpac, idesp, data, horaincon, horafimcon, formapgto):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
    INSERT INTO hospital.consulta (CRM, IdPac, IdEsp, Data, HoraInCon, HoraFimCon, FormaPgto)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    start_time = time.time()
    cursor.execute(query, (crm, idpac, idesp, data, horaincon, horafimcon, formapgto))
    conn.commit()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da inserção: {end_time - start_time:.10f} segundos")

def insert_patient(idpaciente, nomepac, cpf, idade, sexo, telefonepac, endereco):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
    INSERT INTO hospital.paciente (idpaciente, NomePac, CPF, Idade, Sexo, TelefonePac, Endereco)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    
    start_time = time.time()
    cursor.execute(query, (idpaciente, nomepac, cpf, idade, sexo, telefonepac, endereco))
    conn.commit()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da inserção: {end_time - start_time:.10f} segundos")

def delete_consulta(idconsulta):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = "DELETE FROM hospital.consulta WHERE idconsulta = %s"
    
    start_time = time.time()
    cursor.execute(query, (idconsulta,))
    conn.commit()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da exclusão: {end_time - start_time:.10f} segundos")

def update_consulta_field(idconsulta, field, value):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = f"UPDATE hospital.consulta SET {field} = %s WHERE idconsulta = %s"
    
    start_time = time.time()
    cursor.execute(query, (value, idconsulta))
    conn.commit()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da atualização: {end_time - start_time:.10f} segundos")

def search_all_consults_by_cpf_normalizada(cpf):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
    SELECT c.idconsulta, p.NomePac, m.NomeM, c.Data, m.CRM, e.NomeE
    FROM hospital.consulta c
    JOIN hospital.paciente p ON c.IdPac = p.idpaciente
    JOIN hospital.medico m ON c.CRM = m.CRM
    JOIN hospital.especialidade e ON c.IdEsp = e.idEsp
    WHERE p.CPF = %s
    """
    
    start_time = time.time()
    cursor.execute(query, (cpf,))
    result = cursor.fetchall()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da consulta: {end_time - start_time:.4f} segundos")
    return result


def search_all_consults_by_cpf(cpf):
    conn = connect_to_database()
    cursor = conn.cursor()
    query = """
    SELECT idconsulta, NomePac, NomeM, Data, CRM, NomeE,
    FROM hospital.consulta_detalhada
    WHERE CPF = %s
    """
    
    start_time = time.time()
    cursor.execute(query, (cpf,))
    result = cursor.fetchall()
    end_time = time.time()
    
    conn.close()
    
    print(f"Tempo de execução da consulta: {end_time - start_time:.4f} segundos")
    return result